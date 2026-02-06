import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url="https://gist.githubusercontent.com/chanwutk/61eb62164abce3d1f254867e238f153f/raw/seattle-weather.csv"
# Load the weather CSV (make sure the file exists in your project folder)
weather = pd.read_csv(url)

# Check the first few rows and column names
print(weather.head())
print("\nColumns:", weather.columns)

# Convert the date column to datetime type
weather['date'] = pd.to_datetime(weather['date'])

# Find basic stats
print("\nAverage Max Temperature:", weather['temp_max'].mean())
print("Average Min Temperature:", weather['temp_min'].mean())
print("Highest Max Temp:", weather['temp_max'].max())
print("Lowest Min Temp:", weather['temp_min'].min())

# Plot daily max and min temperature
plt.figure(figsize=(12, 6))
plt.plot(weather['date'], weather['temp_max'], label='Max Temperature')
plt.plot(weather['date'], weather['temp_min'], label='Min Temperature')
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Seattle Daily Temperature Trends")
plt.legend()
plt.show()

# Plot precipitation
plt.figure(figsize=(12, 5))
sns.barplot(x='date', y='precipitation', data=weather)
plt.title("Daily Precipitation")
plt.xticks(rotation=90)
plt.show()
