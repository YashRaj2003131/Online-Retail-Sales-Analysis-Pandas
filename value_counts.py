import pandas as pd

df = pd.read_csv('online_retail.csv')

category_sales = df.groupby('Category')['Quantity'].sum()
print('Most Sold Category:', category_sales.idxmax())
print('Quantity Sold:', category_sales.max())

popular_city = df.groupby('City')['CustomerName'].count()
print('Most popular city is:', popular_city.idxmax())

no_of_category = df.groupby('Category')['Product'].count().sort_values(ascending=False)
print(no_of_category)