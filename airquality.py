import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
air = pd.read_csv("monthly-averages.csv")

# Show columns and first few rows
print("Columns:", air.columns)
print(air.head())

# Convert Month to datetime (DD-MM-YYYY format)
air['Month'] = pd.to_datetime(air['Month'], dayfirst=True)

# Plot PM2.5 over time (Roadside)
plt.figure(figsize=(12,6))
plt.plot(air['Month'], air['London Mean Roadside PM2.5 Particulate (ug/m3)'], marker='o', color='red')
plt.title("Monthly Roadside PM2.5 Levels in London")
plt.xlabel("Month")
plt.ylabel("PM2.5 (ug/m3)")
plt.xticks(rotation=45)
plt.show()

# Plot PM2.5 over time (Background)
plt.figure(figsize=(12,6))
plt.plot(air['Month'], air['London Mean Background PM2.5 Particulate (ug/m3)'], marker='o', color='green')
plt.title("Monthly Background PM2.5 Levels in London")
plt.xlabel("Month")
plt.ylabel("PM2.5 (ug/m3)")
plt.xticks(rotation=45)
plt.show()

# PM2.5 Distribution (Roadside)
plt.figure(figsize=(10,5))
sns.histplot(air['London Mean Roadside PM2.5 Particulate (ug/m3)'], bins=20, kde=True)
plt.title("Distribution of Roadside PM2.5")
plt.xlabel("PM2.5 (ug/m3)")
plt.show()
