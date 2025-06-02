# Task 1: Data Cleaning and Preprocessing

## Dataset Used
Customer Personality Analysis - Kaggle

## Changes Made:
- Removed missing values using `dropna()`.
- Removed duplicate rows using `drop_duplicates()`.
- Standardized text columns like "Education" and "Marital_Status".
- Renamed columns to be lowercase and use underscores.
- Converted "Dt_Customer" column to datetime format (dd-mm-yyyy).
- Converted numeric columns to appropriate data types.
- Saved cleaned data to `cleaned_marketing_campaign.csv`.

## Tools Used
- Python
- Pandas

## Libraries
- pandas
- numpy
- matplotlib
- seaborn

## Run the Script
```bash

pip install pandas numpy matplotlib seaborn
python Task1.py

