import os
import joblib
import pandas as pd

from sklearn.ensemble import IsolationForest
from sklearn.metrics import confusion_matrix, classification_report

# ----------------------------------
# Load Cleaned Dataset
# ----------------------------------

df = pd.read_csv("./dataset/cleaned_creditcard.csv")

print("=" * 50)
print("Dataset Loaded Successfully")
print("=" * 50)

print("Dataset Shape:", df.shape)

# ----------------------------------
# Separate Features and Target
# ----------------------------------

X = df.drop("Class", axis=1)
y = df["Class"]

print("Number of Features:", X.shape[1])

# ----------------------------------
# Train Isolation Forest
# ----------------------------------

print("\nTraining Isolation Forest...")

model = IsolationForest(
    n_estimators=100,
    contamination=0.0017,
    random_state=42
)

model.fit(X)

print("Training Completed!")

# ----------------------------------
# Predict
# ----------------------------------

predictions = model.predict(X)

# Convert predictions
# Isolation Forest:
#  1  -> Normal
# -1 -> Anomaly
#
# Dataset:
# 0 -> Normal
# 1 -> Fraud

predictions = [1 if p == -1 else 0 for p in predictions]

# ----------------------------------
# Evaluation
# ----------------------------------

print("\nConfusion Matrix")
print(confusion_matrix(y, predictions))

print("\nClassification Report")
print(classification_report(y, predictions))

# ----------------------------------
# Save Model
# ----------------------------------

os.makedirs("./models", exist_ok=True)

joblib.dump(model, "./models/isolation_forest.pkl")

print("\nModel Saved Successfully!")
print("Location: ./models/isolation_forest.pkl")