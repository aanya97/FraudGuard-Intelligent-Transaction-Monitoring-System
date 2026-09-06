import pandas as pd

# -----------------------------
# Load Dataset
# -----------------------------

df = pd.read_csv("./dataset/creditcard.csv")

print("=" * 60)
print("Dataset Loaded Successfully")
print("=" * 60)

# -----------------------------
# Dataset Shape
# -----------------------------

print("\nDataset Shape:")
print(df.shape)

# -----------------------------
# Column Names
# -----------------------------

print("\nColumns:")
print(df.columns.tolist())

# -----------------------------
# Data Types
# -----------------------------

print("\nData Types:")
print(df.dtypes)

# -----------------------------
# First Five Rows
# -----------------------------

print("\nFirst Five Rows:")
print(df.head())

# -----------------------------
# Last Five Rows
# -----------------------------

print("\nLast Five Rows:")
print(df.tail())

# -----------------------------
# Statistical Summary
# -----------------------------

print("\nStatistical Summary:")
print(df.describe())

# -----------------------------
# Missing Values
# -----------------------------

print("\nMissing Values:")
print(df.isnull().sum())

# -----------------------------
# Duplicate Rows
# -----------------------------

duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

# -----------------------------
# Class Distribution
# -----------------------------

print("\nClass Distribution:")

print(df["Class"].value_counts())

print("\nClass Percentage:")

print(df["Class"].value_counts(normalize=True) * 100)