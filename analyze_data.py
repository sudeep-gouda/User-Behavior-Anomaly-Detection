import pandas as pd

df = pd.read_csv("data/user_behavior.csv")


print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Dataset Information ---")
print(df.info())

print("\n--- Statistical Summary ---")
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Average User Behavior ---")
print(df[[
    "login_hour",
    "files_accessed",
    "failed_logins",
    "data_downloaded_mb"
]].mean())


suspicious = df[
    (df["login_hour"] < 6) |
    (df["failed_logins"] >= 4) |
    (df["files_accessed"] > 100) |
    (df["data_downloaded_mb"] > 1000)
]

print("\n--- Suspicious Activities ---")
print(suspicious)

print(f"\nTotal suspicious records: {len(suspicious)}")