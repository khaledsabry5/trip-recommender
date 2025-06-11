import pandas as pd
import numpy as np
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
from math import radians, sin, cos, sqrt, atan2
from models import RecommendationRequest

def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Earth's radius in km
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    return R * c

def recommend_trips(request: RecommendationRequest):
    # Extract data from request
    user_id = request.user_id
    user_lat = request.latitude
    user_lon = request.longitude
    past_trip_ids = request.past_trip_ids
    trips = request.trips
    locations = request.locations

    # Convert to DataFrame and dictionary
    trips_df = pd.DataFrame([t.dict() for t in trips])
    locations_dict = {loc.Id: (loc.Latitude, loc.Longitude) for loc in locations}

    # Preprocess trip data
    trips_df['DepartureTime'] = pd.to_datetime(trips_df['DepartureTime'])
    trips_df['Hour'] = trips_df['DepartureTime'].dt.hour
    trips_df['DayOfWeek'] = trips_df['DepartureTime'].dt.dayofweek

    categorical_cols = ['FromLocationId', 'ToLocationId']
    numerical_cols = ['PricePerSeat', 'EstimatedDistance', 'EstimatedDuration', 'Hour', 'DayOfWeek']
    binary_cols = ['HasAirConditioning', 'HasFreeWater', 'HasMusic', 'HasPhoneCharger', 'HasWiFi']

    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols),
            ('num', StandardScaler(), numerical_cols),
            ('bin', 'passthrough', binary_cols)
        ]
    )

    feature_matrix = preprocessor.fit_transform(trips_df)
    trip_ids = trips_df['TripId'].values

    # Compute user profile for returning users
    past_trip_indices = [i for i, tid in enumerate(trip_ids) if tid in past_trip_ids]
    user_profile = None
    if past_trip_indices:
        past_features = feature_matrix[past_trip_indices]
        user_profile = np.mean(past_features, axis=0)

    # Calculate scores for each trip
    scores = []
    for idx, trip in trips_df.iterrows():
        from_loc_id = trip['FromLocationId']
        if from_loc_id in locations_dict:
            from_lat, from_lon = locations_dict[from_loc_id]
            distance = haversine(user_lat, user_lon, from_lat, from_lon)
            distance_score = np.exp(-distance / 50)  # Exponential decay with sigma=50

            if user_profile is not None:
                similarity = cosine_similarity(user_profile.reshape(1, -1), feature_matrix[idx].reshape(1, -1))[0][0]
                final_score = 0.5 * similarity + 0.5 * distance_score  # Weighted combination
            else:
                final_score = distance_score  # New users: distance only

            scores.append((trip['TripId'], final_score))

    # Return top 5 trip IDs
    scores.sort(key=lambda x: x[1], reverse=True)
    return [tid for tid, _ in scores[:5]]