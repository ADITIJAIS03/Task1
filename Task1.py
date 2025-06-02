import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv('marketing_campaign.csv', sep='\t')  # the CSV is tab-separated

# Step 2: Overview of the data
print("Initial shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())

# Step 3: Handling missing values
df = df.dropna()  # Alternatively, use df.fillna(method='ffill') if appropriate

# Step 4: Remove duplicate rows
df = df.drop_duplicates()

# Step 5: Standardize text columns
df['Education'] = df['Education'].str.strip().str.title()
df['Marital_Status'] = df['Marital_Status'].str.strip().str.title()

# Step 6: Fix column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Step 7: Convert date column
df['dt_customer'] = pd.to_datetime(df['dt_customer'], format='%d-%m-%Y')

# Step 8: Fix data types
df['income'] = pd.to_numeric(df['income'], errors='coerce')  # handle non-numeric issues
df['kidhome'] = df['kidhome'].astype(int)
df['teenhome'] = df['teenhome'].astype(int)


# Step 9: Save cleaned data
df.to_csv('cleaned_marketing_campaign.csv', index=False)

print("\nCleaned shape:", df.shape)
print("Data cleaning complete. Cleaned file saved as 'cleaned_marketing_campaign.csv'.")
