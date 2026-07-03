import pandas as pd

df = pd.read_csv('online_retail.csv')

# Show only Electronics orders.
electronics_order = df[df['Category'] == 'Electronics']
print(electronics_order)

# Show orders from Mumbai.
mumbai_order = df[df['City'] == 'Mumbai']
print(mumbai_order)

# Show products costing more than ₹5000.
products = df[df['Price'] > 5000]
print(products)

# Show orders where discount is greater than 10%.
discount = df[df['Discount'] > 0.10]
print(discount)

# Find all orders by Amit.
amit_orders = df[df['CustomerName'] == 'Amit']
print(amit_orders)