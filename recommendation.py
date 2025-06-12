import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from math import radians, sin, cos, sqrt, atan2
import datetime
from models import Location, Trip, RecommendationRequest

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

def recommend_trips(request: RecommendationRequest):
    # 1. Unpack
    past = request.past_trips
    upcoming = request.upcoming_trips
    locs = request.locations

    # 2. Model → dicts
    past_df = pd.DataFrame([t.dict() for t in past])
    upcoming_df = pd.DataFrame([t.dict() for t in upcoming])

    # 3. Tag and combine
    if not past_df.empty:
        past_df["is_past"] = True
    if not upcoming_df.empty:
        upcoming_df["is_past"] = False

    all_trips = pd.concat([past_df, upcoming_df], ignore_index=True)
    if all_trips.empty:
        return []

    # 4. Temporal features
    all_trips["DepartureTime"] = pd.to_datetime(all_trips["DepartureTime"])
    all_trips["Hour"]      = all_trips["DepartureTime"].dt.hour
    all_trips["DayOfWeek"] = all_trips["DepartureTime"].dt.dayofweek

    # 5. Build our transformer
    all_ids = [loc.Id for loc in locs]
    cat_cols = ["FromLocationId", "ToLocationId"]
    num_cols = ["PricePerSeat", "EstimatedDistance", "EstimatedDuration", "Hour", "DayOfWeek"]
    bin_cols = ["HasAirConditioning", "HasFreeWater", "HasMusic", "HasPhoneCharger", "HasWiFi"]

    preprocessor = ColumnTransformer([
        ("cat", OneHotEncoder(
            categories=[all_ids, all_ids],
            handle_unknown="ignore"
        ), cat_cols),
        ("num", StandardScaler(), num_cols),
        ("bin", "passthrough", bin_cols),
    ])

    features = preprocessor.fit_transform(all_trips)

    # 6. User profile from past trips
    user_profile = None
    if len(past) > 0:
        user_profile = features[: len(past) ].mean(axis=0)

    # 7. Filter “real” upcoming
    now = datetime.datetime.now()
    mask = (
        (all_trips["is_past"] == False) &
        (all_trips["DepartureTime"] > now) &
        (all_trips["AvailableSeats"] > 0)
    )
    eligible = all_trips[mask]
    if eligible.empty:
        return []

    # 8. Spatial scoring
    loc_dict = {loc.Id: (loc.Latitude, loc.Longitude) for loc in locs}
    scores = []
    for idx, trip in eligible.iterrows():
        fx = features[idx]
        lat, lon = loc_dict[trip["FromLocationId"]]
        d = haversine(request.latitude, request.longitude, lat, lon)
        dist_score = np.exp(-d / 50)

        if user_profile is not None:
            sim = cosine_similarity(user_profile.reshape(1, -1), fx.reshape(1, -1))[0, 0]
            score = 0.5 * sim + 0.5 * dist_score
        else:
            score = dist_score

        scores.append((trip["TripId"], score))

    # 9. Return top-5
    top5 = sorted(scores, key=lambda x: x[1], reverse=True)[:5]
    return [trip_id for trip_id, _ in top5]
