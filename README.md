File models.py:
This file defines the structure of the JSON data the API expects.
File recommendation.py:
This file contains the logic to process the incoming JSON data and generate trip recommendations.


How It Works:
Request Format: The API expects a POST request to /recommend_trips with a JSON body containing:
user_id: A string identifying the user.
latitude and longitude: The user's current location.
past_trip_ids: A list of trip IDs the user has taken (empty for new users).
trips: A list of trip objects with features like price, distance, and amenities.
locations: A list of location objects with IDs and coordinates.
Processing:
For new users (past_trip_ids is empty), recommendations are based on the distance from their location to each trip’s starting point.
For returning users, the API combines distance with content-based similarity, using past trip features.
Response: Returns a JSON object with the user_id and a list of up to 5 recommended TripIds.

Example JSON body:
{
    "user_id": "user1",
    "latitude": 35.0,
    "longitude": -75.0,
    "past_trip_ids": [1],
    "trips": [
        {"TripId": 1, "FromLocationId": 1, "ToLocationId": 2, "PricePerSeat": 10.0, "EstimatedDistance": 50.0, "EstimatedDuration": 1.0, "DepartureTime": "2023-12-01T08:00:00",
        "HasAirConditioning": 1, "HasFreeWater": 0, "HasMusic": 1, "HasPhoneCharger": 0, "HasWiFi": 1},
        {"TripId": 2, "FromLocationId": 3, "ToLocationId": 4, "PricePerSeat": 15.0, "EstimatedDistance": 70.0, "EstimatedDuration": 1.5, "DepartureTime": "2023-12-01T09:00:00",
        "HasAirConditioning": 0, "HasFreeWater": 1, "HasMusic": 0, "HasPhoneCharger": 1, "HasWiFi": 0}
    ],
    "locations": [
        {"Id": 1, "Latitude": 35.0, "Longitude": -75.0},
        {"Id": 2, "Latitude": 36.0, "Longitude": -76.0},
        {"Id": 3, "Latitude": 37.0, "Longitude": -77.0},
        {"Id": 4, "Latitude": 38.0, "Longitude": -78.0}
    ]
}
