import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/anomaly_results.csv")

status_counts = df["status"].value_counts()

plt.figure(figsize=(7, 5))
status_counts.plot(kind="bar")
plt.title("Normal vs Anomalous Activities")
plt.xlabel("Activity Status")
plt.ylabel("Number of Records")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("data/normal_vs_anomaly.png")
plt.show()

plt.figure(figsize=(8, 5))

plt.hist(
    df[df["status"] == "Normal"]["login_hour"],
    bins=20,
    alpha=0.7,
    label="Normal"
)

plt.hist(
    df[df["status"] == "Anomaly"]["login_hour"],
    bins=20,
    alpha=0.7,
    label="Anomaly"
)

plt.title("Login Hour Distribution")
plt.xlabel("Login Hour")
plt.ylabel("Number of Activities")
plt.legend()
plt.tight_layout()
plt.savefig("data/login_hour_distribution.png")
plt.show()

user_downloads = df.groupby("user")["data_downloaded_mb"].sum()

plt.figure(figsize=(8, 5))
user_downloads.plot(kind="bar")
plt.title("Total Data Downloaded by User")
plt.xlabel("User")
plt.ylabel("Data Downloaded (MB)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("data/user_downloads.png")
plt.show()

plt.figure(figsize=(8, 5))

normal = df[df["status"] == "Normal"]
anomaly = df[df["status"] == "Anomaly"]

plt.scatter(
    normal["files_accessed"],
    normal["data_downloaded_mb"],
    alpha=0.5,
    label="Normal"
)

plt.scatter(
    anomaly["files_accessed"],
    anomaly["data_downloaded_mb"],
    alpha=0.7,
    label="Anomaly"
)

plt.title("Files Accessed vs Data Downloaded")
plt.xlabel("Files Accessed")
plt.ylabel("Data Downloaded (MB)")
plt.legend()
plt.tight_layout()
plt.savefig("data/files_vs_download.png")
plt.show()

plt.figure(figsize=(8, 5))

plt.hist(
    df["anomaly_score"],
    bins=30
)

plt.title("Anomaly Score Distribution")
plt.xlabel("Anomaly Score")
plt.ylabel("Number of Records")
plt.tight_layout()
plt.savefig("data/anomaly_score_distribution.png")
plt.show()

print("Visualization completed successfully!")
print("Charts saved inside the data folder.")