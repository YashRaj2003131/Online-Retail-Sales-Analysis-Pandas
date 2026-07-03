import pandas as pd

df = pd.read_csv('online_retail.csv')

df['Total_Sales'] = df['Quantity'] * df['Price']

# Total sales by category
result_by_category = df.groupby('Category')['Total_Sales'].sum()

# Total sales by city
result_by_city = df.groupby('City')['Total_Sales'].sum()

# Average product price by category
avg_by_category = df.groupby('Category')['Price'].mean()

# Total quantity sold by product
total_qty_by_product = df.groupby('Product')['Quantity'].sum()

# Maximum priced product in each category
result = df.loc[df.groupby('Category')['Price'].idxmax()]

print(result)