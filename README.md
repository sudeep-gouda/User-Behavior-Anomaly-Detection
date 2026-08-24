# User Behavior Anomaly Detection

A machine learning project that analyzes user activity patterns and detects unusual or potentially suspicious behavior.

## Project Overview

This project uses user behavior data such as:

- Login hour
- Number of files accessed
- Failed login attempts
- Amount of data downloaded

Machine learning is used to identify abnormal behavior and classify user activity as **Normal** or **Anomaly**.

The project also includes a Streamlit dashboard for visualizing the detected anomalies.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Machine Learning
- Git & GitHub

## Project Structure

```text
User-Behavior-Anomaly-Detection/
│
├── analyze_data.py
├── dashboard.py
├── generate_data.py
├── ml_model.py
├── visualize.py
├── anomaly_results.csv
├── user_behavior.csv
│
├── data/
│   └── .gitkeep
│
├── anomaly_score_distribution.png
├── files_vs_download.png
├── login_hour_distribution.png
├── normal_vs_anomaly.png
└── user_downloads.png
```

## How It Works

### 1. Generate Data

`generate_data.py` creates user behavior data for analysis.

### 2. Analyze Data

`analyze_data.py` performs basic analysis and prepares the data.

### 3. Machine Learning

`ml_model.py` applies an anomaly detection model to identify unusual user behavior.

### 4. Visualization

`visualize.py` generates charts showing user behavior and detected anomalies.

### 5. Dashboard

`dashboard.py` creates an interactive Streamlit dashboard displaying:

- User behavior statistics
- Visualizations
- Detected anomalies
- Anomaly scores
- Anomaly details

##  How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/sudeep-gouda/User-Behavior-Anomaly-Detection.git
cd User-Behavior-Anomaly-Detection
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows:**

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install pandas numpy scikit-learn matplotlib streamlit
```

### 5. Run the Dashboard

```bash
streamlit run dashboard.py
```

The dashboard will open in your browser.

##  Output

The project produces visualizations for:

- Login hour distribution
- Files accessed vs data downloaded
- Normal vs anomalous activity
- Anomaly score distribution
- User download behavior

##  Purpose

The goal of this project is to demonstrate how machine learning can be used to detect unusual user activity that could potentially indicate security incidents or suspicious behavior.

##  Author

**Sudeep Gouda**

B.Tech – Cyber Security
