import os
import joblib

# Path to the trained model
MODEL_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../ml-service/models/isolation_forest.pkl"
    )
)

print("Loading model...")
print("Model Path:", MODEL_PATH)

# Load model
model = joblib.load(MODEL_PATH)

print("Model Loaded Successfully!")