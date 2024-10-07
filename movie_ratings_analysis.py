# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset from the CSV file
df = pd.read_csv('movie_ratings_data.csv')

# Display the first few rows of the dataset
print("Dataset:")
print(df.head())

# --- Data Analysis ---

# 1. Ratings Distribution (Enhanced Histogram with Density Curve)
plt.figure(figsize=(12, 6))
plt.hist(df['Rating'], bins=10, color='lightblue', edgecolor='black', density=True, alpha=0.7)
df['Rating'].plot(kind='kde', color='red')
plt.title('Distribution of Movie Ratings (Data Analyst: Shazil Shahid)', fontsize=16, fontweight='bold')
plt.xlabel('Rating', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 2. Box Plot: Revenue by Genre
plt.figure(figsize=(12, 6))
genres = df['Genre'].unique()
revenues_by_genre = [df[df['Genre'] == genre]['Revenue'] for genre in genres]
plt.boxplot(revenues_by_genre, labels=genres, patch_artist=True,
            boxprops=dict(facecolor='lightyellow', color='darkgoldenrod'),
            medianprops=dict(color='darkred'))
plt.title('Revenue Distribution by Genre (Data Analyst: Shazil Shahid)', fontsize=16, fontweight='bold')
plt.xlabel('Genre', fontsize=12)
plt.ylabel('Revenue (millions)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 3. Scatter Plot: Votes vs. Rating
plt.figure(figsize=(12, 6))
plt.scatter(df['Votes'], df['Rating'], c=df['Year'], cmap='coolwarm', s=df['Revenue'] * 2, alpha=0.6, edgecolor='black')
plt.colorbar(label='Year')
plt.title('Votes vs. Rating (Size by Revenue) (Data Analyst: Shazil Shahid)', fontsize=16, fontweight='bold')
plt.xlabel('Votes', fontsize=12)
plt.ylabel('Rating', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 4. Stacked Bar Plot: Revenue by Year and Genre
pivot_data = df.pivot_table(values='Revenue', index='Year', columns='Genre', aggfunc='sum').fillna(0)
pivot_data.plot(kind='bar', stacked=True, colormap='tab20c', figsize=(14, 8), edgecolor='black')
plt.title('Revenue by Year and Genre (Data Analyst: Shazil Shahid)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Revenue (millions)', fontsize=12)
plt.legend(title='Genre')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 5. Line Plot with Markers: Average Rating per Year with Trend Line
plt.figure(figsize=(12, 6))
avg_rating_by_year = df.groupby('Year')['Rating'].mean()
years = avg_rating_by_year.index
ratings = avg_rating_by_year.values

plt.plot(years, ratings, marker='o', color='darkblue', linewidth=2, label='Average Rating')
plt.title('Average Movie Rating Over the Years (Data Analyst: Shazil Shahid)', fontsize=16, fontweight='bold')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Rating', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)

# Adding a trend line
z = np.polyfit(years, ratings, 1)
p = np.poly1d(z)
plt.plot(years, p(years), "r--", label='Trend Line')
plt.legend()
plt.tight_layout()
plt.show()

# Display final revenue information by genre
total_revenue_by_genre = df.groupby('Genre')['Revenue'].sum()
print("\nTotal Revenue by Genre:")
print(total_revenue_by_genre)
