import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import calendar as cal
import datetime


# Load the data (update sheet name if needed)
coffeShopSales = r'C:\Users\HP\Documents\Coffee_Shop_Sales.xlsx'
df = pd.read_excel(coffeShopSales)
df.head()

# Display basic information
print("Data Preview:")
print(df.head())
print("\nColumn Names:", df.columns)

# get the month from date and diplay it in different column as month?
import datetime
from datetime import datetime
date_month= {'transaction_date':[]}
df = pd.DataFrame(date_month)
df['transaction_date'] = pd.to_datetime(df['transaction_date'], format="%d-%m-%Y")
df['month_name'] = df['transaction_date'].dt.strftime('%B')
print(df)


# Adjust if format is different

# 1. Best-selling products
sales= {'unit_price':[],'quantity':[]}
df = pd.DataFrame(sales)
df['Sales'] = df['unit_price'] * df['quantity']
print(df)
top_products = df.groupby('product_category')['Sales'].sum().sort_values(ascending=False)
print("\nBest-selling products:")
print(top_products.head())

plt.figure(figsize=(10, 5))
sns.barplot(x=top_products.index[:10], y=top_products.values[:10], palette='viridis')
plt.xticks(rotation=45)
plt.title("Top 10 Best-Selling Products")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.show()

# 2. Sales trends over time
sales_trend = df.groupby(df['Date'].dt.to_period("M"))['Sales'].sum()
print("\nSales Trend Over Time:")
print(sales_trend)

plt.figure(figsize=(10, 5))
sales_trend.plot(marker='o', linestyle='-')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid()
plt.show()

# 3. Peak sales hours (assuming a 'Time' column exists)
df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour
peak_hours = df.groupby('Hour')['Sales'].sum()
print("\nPeak Sales Hours:")
print(peak_hours)

plt.figure(figsize=(10, 5))
sns.lineplot(x=peak_hours.index, y=peak_hours.values, marker='o')
plt.title("Sales by Hour of the Day")
plt.xlabel("Hour of the Day")
plt.ylabel("Total Sales")
plt.xticks(range(0, 24))
plt.grid()
plt.show()

# 4. Customer purchase patterns (assuming a 'Customer ID' column exists)
customer_spending = df.groupby('Customer ID')['Sales'].sum().sort_values(ascending=False)
print("\nTop Spending Customers:")
print(customer_spending.head())

plt.figure(figsize=(10, 5))
sns.barplot(x=customer_spending.index[:10], y=customer_spending.values[:10], palette='coolwarm')
plt.xticks(rotation=45)
plt.title("Top 10 Customers by Spending")
plt.xlabel("Customer ID")
plt.ylabel("Total Sales")
plt.show()


