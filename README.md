🚲 Seoul Bike Sharing Demand – Exploratory Data Analysis
📌 Project Overview

This project performs Exploratory Data Analysis (EDA) on the Seoul Bike Sharing dataset to understand how environmental and temporal factors influence daily bike rental demand. The analysis uses Python and standard data science libraries to clean, analyse, and visualise real-world data.

The goal is to identify key patterns and relationships that can help improve operational and demand forecasting decisions in urban mobility systems.

📊 Dataset Description

The dataset contains daily records of bike rentals in Seoul, South Korea, along with environmental and seasonal variables such as:

Temperature
Humidity / Dew Point
Wind speed
Visibility
Solar radiation
Rainfall / snowfall
Season and holiday indicators
Bike rental count (target variable)
🛠️ Tools & Libraries Used
Python
Pandas – data manipulation
NumPy – statistical analysis
Matplotlib – data visualisation
🧹 Data Cleaning

The dataset was preprocessed to ensure data quality:

Removed missing (NaN) values
Checked and removed invalid or inconsistent entries
Verified data types for numerical analysis
Ensured dataset consistency for reliable visualisation
📈 Key Analyses Performed
1. Numerical Analysis

Statistical measures (mean, median, standard deviation) were computed for key variables such as temperature, humidity, and bike rental counts to understand central tendency and variability.

2. Simple Plot Analysis

A scatter/line plot was used to explore relationships between environmental factors (e.g., temperature) and bike rental demand. This helped identify general trends in user behaviour.

3. Multi-variable Analysis

A multi-dimensional plot was created using:

Position (x, y variables)
Colour mapping
Marker size variation

This allowed deeper insights into how multiple environmental factors jointly influence bike demand.

🔍 Key Insights
Bike rental demand shows clear dependence on environmental conditions such as temperature and weather.
Moderate temperatures are associated with higher rental activity.
Extreme weather conditions (e.g., low visibility, high precipitation) significantly reduce demand.
Seasonal and time-based patterns play an important role in user behaviour.
🚀 Extension Analysis

An additional analysis was performed using correlation-based exploration to identify relationships between multiple variables simultaneously. This provided deeper insights into how environmental factors interact to influence bike usage patterns.

🎯 Conclusion

This project demonstrates a full data analysis workflow including data cleaning, statistical analysis, and multi-variable visualisation. The findings highlight how environmental conditions significantly influence urban bike-sharing demand.

📌 Author

Thien Ngan Nguyen
Exploratory Data Analysis Project – Macquarie University
