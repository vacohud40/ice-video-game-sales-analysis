# ice-video-game-sales-analysis
This project analyzes video game sales data from 2016 and earlier to identify patterns that determine a game's success.  The goal is to provide insights into potentially profitable games for future marketing campaigns.

## Table of Contents

- [Project Description](#project-description)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [App Overview](#app-overview)
- [How to Run the App](#how-to-run-the-app)
- [Key Findings](#key-findings)
- [Conclusion](#conclusion)

## Project Description

This project was developed for the Ice online store, which sells video games globally. By analyzing historical sales data, user and expert reviews, genres, platforms, and ESRB ratings, we aim to identify factors that contribute to a game's success. This information will be used to spot potential big winners and plan advertising campaigns.

## Dataset

The dataset used in this analysis is `games.csv`. It contains information on video games released up to 2016, including:

- Name: Name of the game
- Platform: Gaming platform (e.g., Xbox, PlayStation)
- Year_of_Release: Year of release
- Genre: Game genre (e.g., Action, Sports)
- NA_Sales: North American sales (in millions of USD)
- EU_Sales: European sales (in millions of USD)
- JP_Sales: Japanese sales (in millions of USD)
- Other_Sales: Sales in other regions (in millions of USD)
- Critic_Score: Critic score (out of 100)
- User_Score: User score (out of 10)
- Rating: ESRB rating

The dataset can be found in the project repository as `games.csv`.

## Methodology

The analysis involved the following steps:

1. **Data Cleaning and Preprocessing:** Handling missing values, converting data types, and calculating total sales.
2. **Exploratory Data Analysis:** Analyzing sales trends by year, platform, and genre.  Creating visualizations to understand sales distributions.
3. **Regional Analysis:** Examining sales patterns in North America, Europe, and Japan.
4. **Correlation Analysis:** Investigating the relationship between reviews (user and critic) and sales.
5. **Building a Streamlit App:** Creating an interactive web application to visualize the findings and allow users to explore the data.

## App Overview

The Streamlit app (`app.py`) provides an interactive interface to explore the video game sales data.  Users can:

- Filter data by platform, genre, and year range.
- View charts showing game releases per year, platform sales, sales by genre, and sales distribution by platform.
- See key insights derived from the analysis.
- Read the overall conclusion of the project.

## How to Run the App

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/vacohud40/ice-video-game-sales-analysis](https://github.com/vacohud40/ice-video-game-sales-analysis)  
   cd ice-video-game-sales-analysis