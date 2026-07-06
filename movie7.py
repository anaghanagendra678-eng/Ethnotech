import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

url="https://raw.githubusercontent.com/JaviRute/top_1000_movies-data_science_project/main/imdb_top_1000.csv"
# Load dataset
movies = pd.read_csv(url)

# Show columns and sample data
print("Columns:", movies.columns)
print(movies.head())

# Rename columns for convenience
movies = movies.rename(columns={
    "Series_Title": "Title",
    "IMDB_Rating": "Rating",
    "Released_Year": "Year"
})

# 1) Top 10 movies by rating
top10 = movies.sort_values(by="Rating", ascending=False).head(10)
print("\nTop 10 Movies by Rating:")
print(top10[["Title", "Rating", "Year"]])

# 2) Rating distribution
plt.figure(figsize=(10,6))
sns.histplot(movies["Rating"], bins=20, kde=True)
plt.title("Distribution of IMDb Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.show()

# 3) Rating vs Year
plt.figure(figsize=(10,6))
sns.scatterplot(data=movies, x="Year", y="Rating")
plt.title("IMDb Rating vs Released Year")
plt.xlabel("Year")
plt.ylabel("Rating")
plt.show()
