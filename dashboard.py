import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/anomaly_results.csv")

st.set_page_config(
    page_title="User Behavior Anomaly Detection",
    layout="wide"
)

st.title("User Behavior Anomaly Detection")
st.write("Machine learning based analysis of user activities")

total = len(df)
anomalies = (df["status"] == "Anomaly").sum()
normal = (df["status"] == "Normal").sum()

col1, col2, col3 = st.columns(3)

col1.metric("Total Activities", total)
col2.metric("Normal Activities", normal)
col3.metric("Anomalies Detected", anomalies)

st.subheader("Activity Status")

status_counts = df["status"].value_counts()

fig, ax = plt.subplots()
status_counts.plot(kind="bar", ax=ax)
ax.set_xlabel("Status")
ax.set_ylabel("Number of Records")
st.pyplot(fig)

st.subheader("User Activity")

user = st.selectbox(
    "Select User",
    df["user"].unique()
)

user_data = df[df["user"] == user]

st.dataframe(user_data, use_container_width=True)

st.subheader("Files Accessed vs Data Downloaded")

fig, ax = plt.subplots()

normal_data = df[df["status"] == "Normal"]
anomaly_data = df[df["status"] == "Anomaly"]

ax.scatter(
    normal_data["files_accessed"],
    normal_data["data_downloaded_mb"],
    label="Normal"
)

ax.scatter(
    anomaly_data["files_accessed"],
    anomaly_data["data_downloaded_mb"],
    label="Anomaly"
)

ax.set_xlabel("Files Accessed")
ax.set_ylabel("Data Downloaded (MB)")
ax.legend()

st.pyplot(fig)

st.subheader("Detected Anomalies")

anomalies_df = df[df["status"] == "Anomaly"]

st.dataframe(
    anomalies_df,
    width="stretch"
)