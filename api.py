from fastapi import FastAPI
from models import RecommendationRequest
from recommendation import recommend_trips

app = FastAPI()

@app.post("/recommend_trips")
def get_recommendations(request: RecommendationRequest):
    recommended_trips = recommend_trips(request)
    return {"user_id": request.user_id, "recommended_trips": recommended_trips}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)