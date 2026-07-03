import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('online_retail.csv')

df['Total'] = df['Quantity'] * df['Price']

# Bar Chart of Sales 
sales_by_category = df.groupby('Category')['Total'].sum().sort_values(ascending=False)

sales_by_category.plot(kind='bar')

plt.title('Sales by Category')
plt.xlabel('Category')
plt.ylabel('Total Sales')

plt.show()

# Pie Chart of Category Distribution
category_distribution = df['Category'].value_counts()

category_distribution.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title('Category Distribution')
plt.ylabel('')
plt.show()

