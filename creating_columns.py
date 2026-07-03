import pandas as pd

df = pd.read_csv('online_retail.csv')

# Create a new column
# Total = Quantity × Price
df['Total'] = df['Quantity'] * df['Price']

# Create another column
# FinalAmount = Total - (Total × Discount)
df['FinalAmount'] = df['Total'] - (df['Total'] * df['Discount'])

print(df)