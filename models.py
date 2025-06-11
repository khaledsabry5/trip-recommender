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
    DepartureTime: str  # ISO format, e.g., "2023-12-01T08:00:00"
    HasAirConditioning: int
    HasFreeWater: int
    HasMusic: int
    HasPhoneCharger: int
    HasWiFi: int

class RecommendationRequest(BaseModel):
    user_id: str
    latitude: float
    longitude: float
    past_trip_ids: List[int]
    trips: List[Trip]
    locations: List[Location]


"""
Example JSON body:

{
    "user_id": "user1",
    "latitude": 35.0,
    "longitude": -75.0,
    "past_trip_ids": [1],
    "trips": [
        {"TripId": 1, "FromLocationId": 1, "ToLocationId": 2, "PricePerSeat": 10.0, "EstimatedDistance": 141.0, "EstimatedDuration": 2.82, "DepartureTime": "2025-06-12T08:00:00", "HasAirConditioning": 1, "HasFreeWater": 0, "HasMusic": 1, "HasPhoneCharger": 0, "HasWiFi": 1},
        {"TripId": 2, "FromLocationId": 3, "ToLocationId": 4, "PricePerSeat": 15.0, "EstimatedDistance": 141.0, "EstimatedDuration": 2.82, "DepartureTime": "2025-06-12T09:00:00", "HasAirConditioning": 0, "HasFreeWater": 1, "HasMusic": 0, "HasPhoneCharger": 1, "HasWiFi": 0},
        {"TripId": 3, "FromLocationId": 2, "ToLocationId": 1, "PricePerSeat": 12.0, "EstimatedDistance": 141.0, "EstimatedDuration": 2.82, "DepartureTime": "2025-06-12T10:00:00", "HasAirConditioning": 0, "HasFreeWater": 1, "HasMusic": 0, "HasPhoneCharger": 1, "HasWiFi": 0},
        {"TripId": 4, "FromLocationId": 4, "ToLocationId": 3, "PricePerSeat": 18.0, "EstimatedDistance": 141.0, "EstimatedDuration": 2.82, "DepartureTime": "2025-06-12T11:00:00", "HasAirConditioning": 1, "HasFreeWater": 0, "HasMusic": 1, "HasPhoneCharger": 0, "HasWiFi": 1},
        {"TripId": 5, "FromLocationId": 1, "ToLocationId": 3, "PricePerSeat": 20.0, "EstimatedDistance": 283.0, "EstimatedDuration": 5.66, "DepartureTime": "2025-06-12T12:00:00", "HasAirConditioning": 1, "HasFreeWater": 1, "HasMusic": 0, "HasPhoneCharger": 0, "HasWiFi": 1},
        {"TripId": 6, "FromLocationId": 2, "ToLocationId": 4, "PricePerSeat": 22.0, "EstimatedDistance": 283.0, "EstimatedDuration": 5.66, "DepartureTime": "2025-06-12T13:00:00", "HasAirConditioning": 0, "HasFreeWater": 0, "HasMusic": 1, "HasPhoneCharger": 1, "HasWiFi": 0},
        {"TripId": 7, "FromLocationId": 3, "ToLocationId": 1, "PricePerSeat": 25.0, "EstimatedDistance": 283.0, "EstimatedDuration": 5.66, "DepartureTime": "2025-06-12T14:00:00", "HasAirConditioning": 1, "HasFreeWater": 0, "HasMusic": 0, "HasPhoneCharger": 1, "HasWiFi": 1},
        {"TripId": 8, "FromLocationId": 4, "ToLocationId": 2, "PricePerSeat": 28.0, "EstimatedDistance": 283.0, "EstimatedDuration": 5.66, "DepartureTime": "2025-06-12T15:00:00", "HasAirConditioning": 0, "HasFreeWater": 1, "HasMusic": 1, "HasPhoneCharger": 0, "HasWiFi": 0},
        {"TripId": 9, "FromLocationId": 1, "ToLocationId": 4, "PricePerSeat": 30.0, "EstimatedDistance": 424.0, "EstimatedDuration": 8.48, "DepartureTime": "2025-06-12T16:00:00", "HasAirConditioning": 1, "HasFreeWater": 1, "HasMusic": 1, "HasPhoneCharger": 0, "HasWiFi": 0},
        {"TripId": 10, "FromLocationId": 2, "ToLocationId": 3, "PricePerSeat": 32.0, "EstimatedDistance": 141.0, "EstimatedDuration": 2.82, "DepartureTime": "2025-06-12T17:00:00", "HasAirConditioning": 0, "HasFreeWater": 0, "HasMusic": 0, "HasPhoneCharger": 1, "HasWiFi": 1}
    ],
    "locations": [
        {"Id": 1, "Latitude": 35.0, "Longitude": -75.0},
        {"Id": 2, "Latitude": 36.0, "Longitude": -76.0},
        {"Id": 3, "Latitude": 37.0, "Longitude": -77.0},
        {"Id": 4, "Latitude": 38.0, "Longitude": -78.0}
    ]
}
"""
