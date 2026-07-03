import pandas as pd

df = pd.read_csv('online_retail.csv')

df['Total'] = df['Quantity'] * df['Price']

df['FinalAmount'] = df['Total'] - (df['Total'] * df['Discount'])

# Which category generated the highest revenue?
highest_category = df.groupby('Category')['FinalAmount'].sum().sort_values(ascending=False)
print('Highest revenue by category is:', highest_category.idxmax())

# Which city generated the highest sales?
highest_city = df.groupby('City')['FinalAmount'].sum().sort_values(ascending=False)
print('Highest revenue by city is:', highest_city.idxmax())

# Which customer spent the most?
most_spent_cust = df.groupby('CustomerName')['FinalAmount'].sum().sort_values(ascending=False)
print('Customer spent the most is:', most_spent_cust.idxmax())

# Which product earned the most money?
most_product_sold = df.groupby('Product')['FinalAmount'].sum().sort_values(ascending=True)
print('Product which are earned the most is:', most_product_sold.idxmax())

# Which products were sold only once?
only_once = df.groupby('Product')['Quantity'].sum()
print('Product that sold only once:\n', only_once[only_once==1])

# Which category had the highest average order value?
highest_order_value = df.groupby('Category')['Quantity'].mean().sort_values(ascending=False)
print('Highest average order value by category:', highest_category.idxmax())