import pandas as pd

df = pd.read_csv('online_retail.csv')

df['Total'] = df['Price'] * df['Quantity']

df['FinalAmount'] = df['Total'] - (df['Total'] * df['Discount'])

# Highest price
print(df[df['Price'] == df['Price'].max()])

# Lowest discount
print(df[df['Discount'] == df['Discount'].min()])

# Highest final amount
print(df[df['FinalAmount'] == df['FinalAmount'].max()])

