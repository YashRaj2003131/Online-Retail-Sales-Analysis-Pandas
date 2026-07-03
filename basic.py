import pandas as pd

# Read the CSV.
df = pd.read_csv('online_retail.csv')
print(df)

# Display first 5 rows.
print(df.head())

# Display last 5 rows.
print(df.tail())

# Find shape.
print(df.shape)

# Find columns.
print(df.columns)

# Find data types.
print(df.info())

# Find missing values.
print(df.isnull().sum())

# Generate descriptive statistics.
print(df.describe())

# Rename a column.
df.rename(columns={'Price':'UnitPrice'}, inplace=True)

# Change OrderDate to datetime.
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

print(df)

