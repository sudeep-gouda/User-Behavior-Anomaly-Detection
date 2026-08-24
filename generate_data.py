import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

users = ["user_01", "user_02", "user_03", "user_04", "user_05"]

data = []

start_date = datetime(2026, 1, 1)

for i in range(500):
    user = random.choice(users)

    date = start_date + timedelta(days=random.randint(0, 180))

    login_hour = random.randint(8, 20)
    files_accessed = random.randint(5, 50)
    failed_logins = random.randint(0, 2)
    data_downloaded_mb = random.randint(50, 500)

    
    if random.random() < 0.10:
        login_hour = random.choice([1, 2, 3, 4, 5])
        files_accessed = random.randint(100, 300)
        failed_logins = random.randint(4, 10)
        data_downloaded_mb = random.randint(1000, 5000)

    data.append([
        user,
        date.strftime("%Y-%m-%d"),
        login_hour,
        files_accessed,
        failed_logins,
        data_downloaded_mb
    ])

df = pd.DataFrame(data, columns=[
    "user",
    "date",
    "login_hour",
    "files_accessed",
    "failed_logins",
    "data_downloaded_mb"
])

df.to_csv("data/user_behavior.csv", index=False)

print("Dataset created successfully!")
print(df.head())