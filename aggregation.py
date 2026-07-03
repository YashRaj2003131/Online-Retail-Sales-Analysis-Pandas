import pandas as pd

df = pd.read_csv('online_retail.csv')

df['Total'] = df['Quantity'] * df['Price']

df['FinalAmount'] = df['Total'] - (df['Total'] * df['Discount'])

total_revenue = df['FinalAmount'].sum()
print('Total revenue:', total_revenue)

avg_order_value = df['Price'].mean()
print('Average order value', avg_order_value)

highest_order_value = df['Price'].max()
print('Highest order value', highest_order_value)

lowest_order_value = df['Price'].min()
print('Highest order value', lowest_order_value)

total_discount = df['Discount'].sum()
print('Total discount given', total_discount)