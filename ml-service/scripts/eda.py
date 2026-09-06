import os
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Create plots folder
# ----------------------------
os.makedirs("../plots", exist_ok=True)

# ----------------------------
# Load dataset
# ----------------------------
df = pd.read_csv("./dataset/creditcard.csv")

print("Dataset Loaded Successfully!")

# ----------------------------
# Histogram of Amount
# ----------------------------
plt.figure(figsize=(8,5))
plt.hist(df["Amount"], bins=50)
plt.title("Transaction Amount Distribution")
plt.xlabel("Amount")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("../plots/amount_distribution.png")
plt.close()

# ----------------------------
# Histogram of Time
# ----------------------------
plt.figure(figsize=(8,5))
plt.hist(df["Time"], bins=50)
plt.title("Transaction Time Distribution")
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("../plots/time_distribution.png")
plt.close()

# ----------------------------
# Class Distribution
# ----------------------------
class_counts = df["Class"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    class_counts,
    labels=["Normal","Fraud"],
    autopct="%1.2f%%",
    startangle=90
)

plt.title("Normal vs Fraud Transactions")
plt.savefig("../plots/class_distribution.png")
plt.close()

# ----------------------------
# Box Plot
# ----------------------------
plt.figure(figsize=(8,5))
plt.boxplot(df["Amount"])
plt.title("Transaction Amount Box Plot")
plt.savefig("../plots/amount_boxplot.png")
plt.close()

print("\nEDA Completed Successfully!")
print("Plots saved inside plots folder.")