import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load MovieLens sample dataset
movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

# Merge movies with their ratings
data = pd.merge(ratings, movies, on="movieId")

# Quick look at data
print(data.head())
print("\nTotal ratings:", len(data))

# Top 10 Movies by Average Rating (minimum 50 ratings)
movie_stats = data.groupby('title')['rating'].agg(['mean','count'])
popular = movie_stats[movie_stats['count'] >= 50]  # at least 50 ratings
top10 = popular.sort_values('mean', ascending=False).head(10)

print("\nTop 10 Movies by Average Rating:")
print(top10)

# Plot distribution of movie ratings
plt.figure(figsize=(10,6))
sns.histplot(data['rating'], bins=10, kde=True)
plt.title("Rating Distribution (MovieLens)")
plt.xlabel("Rating")
plt.show()

# Average ratings by number of ratings
plt.figure(figsize=(12,6))
sns.scatterplot(x='count', y='mean', data=movie_stats)
plt.title("Movie Ratings vs Rating Count")
plt.xlabel("Number of Ratings")
plt.ylabel("Average Rating")
plt.show()
