import pandas as pd
from sklearn.ensemble import IsolationForest

df = pd.read_csv("data/user_behavior.csv")

features = [
    "login_hour",
    "files_accessed",
    "failed_logins",
    "data_downloaded_mb"
]

X = df[features]


model = IsolationForest(
    contamination=0.10,
    random_state=42
)

df["prediction"] = model.fit_predict(X)

df["status"] = df["prediction"].map({
    1: "Normal",
    -1: "Anomaly"
})


df["anomaly_score"] = model.decision_function(X)

print("\n--- ML Anomaly Detection Results ---")
print(df[[
    "user",
    "date",
    "login_hour",
    "files_accessed",
    "failed_logins",
    "data_downloaded_mb",
    "status",
    "anomaly_score"
]].head(20))

print("\n--- Activity Summary ---")
print(df["status"].value_counts())


anomalies = df[df["status"] == "Anomaly"]

print("\n--- Detected Anomalies ---")
print(anomalies[[
    "user",
    "date",
    "login_hour",
    "files_accessed",
    "failed_logins",
    "data_downloaded_mb",
    "anomaly_score"
]])


df.to_csv("data/anomaly_results.csv", index=False)

print("\nResults saved to data/anomaly_results.csv")