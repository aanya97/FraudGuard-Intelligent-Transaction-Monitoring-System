import os
import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------
dataset_path = "./dataset/creditcard.csv"

df = pd.read_csv(dataset_path)

print("=" * 50)
print("Dataset Loaded Successfully")
print("=" * 50)

print(f"Original Shape: {df.shape}")

# -----------------------------
# Missing Values
# -----------------------------
print("\nMissing Values:")

print(df.isnull().sum())

# -----------------------------
# Duplicate Rows
# -----------------------------
duplicates = df.duplicated().sum()

print(f"\nDuplicate Rows: {duplicates}")

# -----------------------------
# Remove Duplicates
# -----------------------------
df = df.drop_duplicates()

print(f"\nShape After Removing Duplicates: {df.shape}")

# -----------------------------
# Save Clean Dataset
# -----------------------------
output_path = "./dataset/cleaned_creditcard.csv"

df.to_csv(output_path, index=False)

# -----------------------------
# Verify File Saved
# -----------------------------
if os.path.exists(output_path):
    print("\n✅ Cleaned dataset saved successfully!")
    print("Location:", os.path.abspath(output_path))
else:
    print("\n❌ Failed to save dataset.")