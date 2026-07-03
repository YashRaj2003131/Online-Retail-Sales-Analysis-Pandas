# Online-Retail-Sales-Analysis-Pandas
Analyzed an online retail sales dataset using Python, Pandas, NumPy, and Matplotlib. Performed data cleaning, filtering, feature engineering, aggregation, business analysis, and visualizations to extract actionable insights.

# 📊 Online Retail Sales Analysis with Pandas

## 📌 Project Overview

This project demonstrates data analysis using **Python** and **Pandas** on an online retail sales dataset.

The objective of this project is to practice data cleaning, filtering, grouping, aggregation, sorting, feature engineering, and visualization using real-world business scenarios.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib

---

## 📂 Dataset Information

The dataset contains the following columns:

- OrderID
- CustomerID
- CustomerName
- Category
- Product
- Quantity
- Price
- Discount
- City
- OrderDate

---

# 📖 Project Tasks

## ✅ Level 1 – Basic Pandas

Performed the following operations:

- Read the CSV file
- Displayed first 5 rows
- Displayed last 5 rows
- Checked dataset shape
- Displayed column names
- Checked data types
- Found missing values
- Generated descriptive statistics
- Renamed a column
- Converted `OrderDate` to datetime format

---

## ✅ Level 2 – Data Filtering

Solved the following business queries:

- Display only Electronics orders
- Display orders from Mumbai
- Display products costing more than ₹5000
- Display orders where discount is greater than 10%
- Find all orders placed by Amit

---

## ✅ Level 3 – Feature Engineering

Created new calculated columns:

### Total

```
Total = Quantity × Price
```

### FinalAmount

```
FinalAmount = Total − (Total × Discount)
```

---

## ✅ Level 4 – Sorting Data

Sorted the dataset by:

- Highest Price
- Lowest Discount
- Highest Final Amount

---

## ✅ Level 5 – GroupBy Analysis

Performed grouped analysis to find:

- Total sales by category
- Total sales by city
- Average product price by category
- Total quantity sold by product
- Maximum priced product in each category

---

## ✅ Level 6 – Aggregation

Calculated:

- Total Revenue
- Average Order Value
- Highest Order Value
- Lowest Order Value
- Total Discount Given

---

## ✅ Level 7 – Customer Analysis

Analyzed customer behavior by finding:

- Customer with highest spending
- Number of orders per customer
- Customer who purchased maximum quantity
- Number of unique customers

---

## ✅ Level 8 – Value Counts

Identified:

- Most sold category
- Most popular city
- Number of products in each category

---

## ✅ Level 9 – Business Insights

Answered important business questions:

- Which category generated the highest revenue?
- Which city generated the highest sales?
- Which customer spent the most?
- Which product earned the most money?
- Which products were sold only once?
- Which category had the highest average order value?

---

## ✅ Level 10 – Data Visualization

Created visualizations using Matplotlib:

- Bar Chart of Sales by Category
- Pie Chart of Category Distribution
- Line Chart of Daily Sales
- Histogram of Product Prices
- Boxplot of Discounts

---

# 📈 Skills Practiced

- Reading CSV Files
- Data Exploration
- Data Cleaning
- Filtering Data
- Creating New Columns
- Sorting
- GroupBy Operations
- Aggregation Functions
- Value Counts
- Business Data Analysis
- DateTime Handling
- Data Visualization

---

# 📚 Pandas Functions Used

```python
read_csv()
head()
tail()
shape
columns
info()
dtypes
describe()
rename()
to_datetime()
groupby()
sort_values()
value_counts()
sum()
mean()
count()
max()
min()
unique()
nunique()
```

---

# 🎯 Learning Outcome

Through this project, I strengthened my understanding of:

- Data manipulation using Pandas
- Business-oriented data analysis
- Customer and sales analytics
- Feature engineering
- Exploratory Data Analysis (EDA)
- Data visualization using Matplotlib

---

## 📌 Author

**Yash Rajbhar**

Aspiring Data Analyst | Python | SQL | Pandas | Power BI | Excel
