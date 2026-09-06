from fastapi import FastAPI
import os
import joblib


app = FastAPI()


MODEL_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../ml-service/models/isolation_forest.pkl"
    )
)


print("Loading model...")
print("Model Path:", MODEL_PATH)


model = joblib.load(MODEL_PATH)


print("Model Loaded Successfully!")


@app.get("/")
def home():
    return {
        "message": "Fraud Detection API Running",
        "model_loaded": True
    }