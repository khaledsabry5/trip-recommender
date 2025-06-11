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