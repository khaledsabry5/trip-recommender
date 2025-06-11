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
