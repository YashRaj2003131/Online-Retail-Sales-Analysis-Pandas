import pandas as pd

df = pd.read_csv('online_retail.csv')

df['Total'] = df['Quantity'] * df['Price']

df['FinalAmount'] = df['Total'] - (df['Total'] * df['Discount'])

highest_spending = df.loc[df['FinalAmount'].idxmax()]
print('Customer with highest spending:', highest_spending['CustomerName'])

no_of_order = df.groupby('CustomerName')['Product'].count()
print('Number of orders per customer:\n', no_of_order)

hightest_qty = df.loc[df['Quantity'].max()]
print('Customer who bought maximum quantity:', highest_spending['CustomerName'])

unique_customers = df['OrderID'].nunique()
print('Number of unique customers:',unique_customers)