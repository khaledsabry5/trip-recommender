from pydantic import BaseModel
from typing import List

class Location(BaseModel):
    Id: int
    Latitude: float
    Longitude: float

class Trip(BaseModel):
    TripId: int
    FromLocationId: int
    ToLocationId: int
    PricePerSeat: float
    EstimatedDistance: float
    EstimatedDuration: float
    DepartureTime: str  # ISO format, e.g., "2025-06-12T08:00:00"
    HasAirConditioning: int
    HasFreeWater: int
    HasMusic: int
    HasPhoneCharger: int
    HasWiFi: int
    AvailableSeats: int

class RecommendationRequest(BaseModel):
    user_id: str
    latitude: float
    longitude: float
    past_trips: List[Trip]
    upcoming_trips: List[Trip]
    locations: List[Location]
    


"""
Example JSON User with Past Trips body:
{
    "user_id": "user1",
    "latitude": 35.0,
    "longitude": -75.0,
    "past_trips": [
        {
            "TripId": 1,
            "FromLocationId": 1,
            "ToLocationId": 2,
            "PricePerSeat": 10.0,
            "EstimatedDistance": 141.0,
            "EstimatedDuration": 2.82,
            "DepartureTime": "2025-06-12T08:00:00",
            "HasAirConditioning": 1,
            "HasFreeWater": 0,
            "HasMusic": 1,
            "HasPhoneCharger": 0,
            "HasWiFi": 1,
            "AvailableSeats": 0
        }
    ],
    "upcoming_trips": [
        {
            "TripId": 2,
            "FromLocationId": 3,
            "ToLocationId": 4,
            "PricePerSeat": 15.0,
            "EstimatedDistance": 141.0,
            "EstimatedDuration": 2.82,
            "DepartureTime": "2025-06-12T12:00:00",
            "HasAirConditioning": 0,
            "HasFreeWater": 1,
            "HasMusic": 0,
            "HasPhoneCharger": 1,
            "HasWiFi": 0,
            "AvailableSeats": 5
        },
        {
            "TripId": 3,
            "FromLocationId": 2,
            "ToLocationId": 1,
            "PricePerSeat": 12.0,
            "EstimatedDistance": 141.0,
            "EstimatedDuration": 2.82,
            "DepartureTime": "2025-06-12T13:00:00",
            "HasAirConditioning": 0,
            "HasFreeWater": 1,
            "HasMusic": 0,
            "HasPhoneCharger": 1,
            "HasWiFi": 0,
            "AvailableSeats": 3
        }
    ],
    "locations": [
        {"Id": 1, "Latitude": 35.0, "Longitude": -75.0},
        {"Id": 2, "Latitude": 36.0, "Longitude": -76.0},
        {"Id": 3, "Latitude": 37.0, "Longitude": -77.0},
        {"Id": 4, "Latitude": 38.0, "Longitude": -78.0}
    ]
}

Example JSON User with NO Past Trips body:
{
    "user_id": "user2",
    "latitude": 36.0,
    "longitude": -76.0,
    "past_trips": [],
    "upcoming_trips": [
        {
            "TripId": 2,
            "FromLocationId": 3,
            "ToLocationId": 4,
            "PricePerSeat": 15.0,
            "EstimatedDistance": 141.0,
            "EstimatedDuration": 2.82,
            "DepartureTime": "2025-06-12T12:00:00",
            "HasAirConditioning": 0,
            "HasFreeWater": 1,
            "HasMusic": 0,
            "HasPhoneCharger": 1,
            "HasWiFi": 0,
            "AvailableSeats": 5
        },
        {
            "TripId": 3,
            "FromLocationId": 2,
            "ToLocationId": 1,
            "PricePerSeat": 12.0,
            "EstimatedDistance": 141.0,
            "EstimatedDuration": 2.82,
            "DepartureTime": "2025-06-12T13:00:00",
            "HasAirConditioning": 0,
            "HasFreeWater": 1,
            "HasMusic": 0,
            "HasPhoneCharger": 1,
            "HasWiFi": 0,
            "AvailableSeats": 3
        }
    ],
    "locations": [
        {"Id": 1, "Latitude": 35.0, "Longitude": -75.0},
        {"Id": 2, "Latitude": 36.0, "Longitude": -76.0},
        {"Id": 3, "Latitude": 37.0, "Longitude": -77.0},
        {"Id": 4, "Latitude": 38.0, "Longitude": -78.0}
    ]
}
"""
