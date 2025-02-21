# Importing libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import plotly.express as px
from scipy import stats
# Opening the data file and studying the general information
df = pd.read_csv('games.csv')
df.head()
# Preparing the data & replacing the columns 
df.columns = df.columns.str.lower()
# Handling missing values

# Name, Genre and Rating: Filled with 'Unknown' 
df['name'].fillna('Unknown', inplace=True)
df['genre'].fillna('Unknown', inplace=True)
df['rating'].fillna('Unknown', inplace=True)
# critic_score, rating and user_score: Filled with 'NaN'
df['critic_score'].fillna('NaN', inplace=True)
df['user_score'].fillna('NaN', inplace=True)
# Remove rows with missing year_of_release (using dropna)
df.dropna(subset=['year_of_release'], inplace=True)
df = df.reset_index(drop=True)

# Converting data types
df['year_of_release'] = pd.to_numeric(df['year_of_release'], errors='coerce')
df['year_of_release'] = df['year_of_release'].astype('Int64')
df['critic_score'] = pd.to_numeric(df['critic_score'], errors='coerce')
df['user_score'] = pd.to_numeric(df['user_score'], errors='coerce')

# Remove duplicate rows (if any) - Keep the first occurrence
df.drop_duplicates(keep='first', inplace=True)

# Calculate total sales
df['total_sales'] = df[['na_sales', 'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)
df.head()

# --- Streamlit App ---

st.title("Video Game Sales Analysis")
st.write("Analysis of video game sales data from 2016 and earlier.")

# --- Filters ---
st.sidebar.subheader("Filters")

platform_filter = st.sidebar.multiselect("Select Platforms", df['platform'].unique())
if not platform_filter:
    platform_filter = df['platform'].unique()

genre_filter = st.sidebar.multiselect("Select Genres", df['genre'].unique())
if not genre_filter:
    genre_filter = df['genre'].unique()

year_filter = st.sidebar.slider("Select Year Range", int(df['year_of_release'].min()), int(df['year_of_release'].max()), (int(df['year_of_release'].min()), int(df['year_of_release'].max())))


# Apply filters
filtered_df = df[df['platform'].isin(platform_filter) & df['genre'].isin(genre_filter) & df['year_of_release'].between(year_filter[0], year_filter[1])]

# --- Charts (Corrected - Using filtered_df consistently) ---

# 1. Games Released Per Year (Filtered)
st.subheader("Games Released Per Year (Filtered)")
games_per_year = filtered_df['year_of_release'].value_counts().sort_index()  # <--- Use filtered_df
fig_games_year = px.bar(games_per_year, x=games_per_year.index, y=games_per_year.values, labels={'x': 'Year', 'y': 'Number of Games'})
st.plotly_chart(fig_games_year)

# 2. Platform Sales (Filtered)
st.subheader("Platform Sales (Filtered)")
platform_sales = filtered_df.groupby('platform')['total_sales'].sum().sort_values(ascending=False) # <--- Use filtered_df
fig_platform_sales = px.bar(platform_sales, x=platform_sales.index, y=platform_sales.values, labels={'x': 'Platform', 'y': 'Total Sales'})
st.plotly_chart(fig_platform_sales)


# 4. Box Plot (Global Sales by Platform)
st.subheader("Box Plot: Global Sales by Platform")
fig_box = px.box(filtered_df, x='platform', y='total_sales', title="Global Sales by Platform") # <--- Use filtered_df
st.plotly_chart(fig_box)

# 5. Sales by Genre (Filtered)
st.subheader("Sales by Genre (Filtered)")
genre_sales = filtered_df.groupby('genre')['total_sales'].sum().sort_values(ascending=False) # <--- Use filtered_df
fig_genre_sales = px.bar(genre_sales, x=genre_sales.index, y=genre_sales.values, labels={'x': 'Genre', 'y': 'Total Sales'})
st.plotly_chart(fig_genre_sales)



# --- Insights and Explanations  ---
st.subheader("Key Insights")
st.write("**Games Released per Year:** A significant growth trend in game releases, peaking around 2008-2011, followed by a decline, but still higher than earlier decades.")

st.write("**Total Sales per Year (1994 Onwards):** Fluctuating but generally upward trend, peaking around 2008-2009, then declining and stabilizing.")

st.write("**Sales Distribution by Year for Top Platforms:** PS2 dominance, X360/PS3 competition, Wii's rise and fall, DS/PSP portable popularity, older platforms fading, recent platforms emerging.")

st.write("**Relevant Period Analysis (2012-2016):** Top platforms: PS4, PS3, X360, 3DS, XOne. PS4 shows growth, PS3/X360/3DS show decline. Negative growth for most established platforms.")

st.write("**Box Plot Observations:** Variability in sales across platforms. PS3/X360 wide IQR, PS4 concentrated distribution. 3DS/WiiU lower median sales.")

st.write("**User/Critic Score Correlation (PS4):** Weak negative correlation between user score and sales. Moderate positive correlation between critic score and sales.")

st.write("**Multi-Platform Sales (Top 10 PS4 Games):** PS4 dominance, varying multi-platform success, PC market relevance, previous generation relevance, franchise strength.")

st.write("**Genre Sales Distribution:** Wide range of sales performance. Shooter/Sports high-performing, Platform/Fighting consistent, Adventure/Puzzle/Strategy lower-performing. Outliers indicate blockbuster games.")

st.write("**Regional Analysis (All Years):** NA: X360, Action. EU: PS2, Action. JP: DS, Role-Playing. Regional differences in platform/genre/rating preferences.")

st.write("**Regional Analysis (2012 Onwards):** NA/EU: PS4, Action/Shooter, M rated. JP: 3DS, Role-Playing, Unknown ratings. Handheld dominance in Japan.")



# --- Conclusion ---
st.subheader("Conclusion")
st.write("This project identified key factors influencing video game sales: platform, genre, region, and reviews. These findings can inform marketing strategies and identify potentially profitable games.")

