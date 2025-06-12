from fastapi import FastAPI
from recommendation import recommend_trips
from models import RecommendationRequest

app = FastAPI()

@app.post("/recommend_trips")
def get_recommendations(request: RecommendationRequest):
    recommended_trips = recommend_trips(request)
    return {"recommended_trips": recommended_trips}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
