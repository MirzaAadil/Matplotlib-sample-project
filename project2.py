import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('company_data.csv')

product_units = df.groupby('Product')['Units_Sold'].sum()
region_sales = df.groupby('Region')['Sales'].sum()
month_sales = df.groupby('Month')['Sales'].sum()

product_units.plot(kind='bar', color='orange')
plt.title('Total Units Sold by Product')
plt.xlabel('Product')
plt.ylabel('Units Sold')
plt.show()

region_sales.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Region-wise Sales Distribution')
plt.ylabel('')
plt.show()

plt.scatter(df['Ad_Budget'], df['Sales'], color='purple')
plt.title('Ad Budget vs Sales')
plt.xlabel('Ad Budget (₹)')
plt.ylabel('Sales (₹)')
plt.show()

plt.hist(df['Sales'], bins=5, color='green', edgecolor='black')
plt.title('Sales Distribution')
plt.xlabel('Sales (₹)')
plt.ylabel('Frequency')
plt.show()

plt.boxplot(df['Sales'])
plt.title('Boxplot of Sales')
plt.ylabel('Sales (₹)')
plt.show()

fig, axs = plt.subplots(2, 2)

month_sales.plot(ax=axs[0, 0], marker='o')
axs[0, 0].set_title('Monthly Sales Trend')
axs[0, 0].set_xlabel('Month')
axs[0, 0].set_ylabel('Total Sales')

product_units.plot(kind='bar', ax=axs[0, 1], color='skyblue')
axs[0, 1].set_title('Units Sold by Product')
axs[0, 1].set_xlabel('Product')
axs[0, 1].set_ylabel('Units Sold')

axs[1, 0].scatter(df['Ad_Budget'], df['Sales'], color='purple')
axs[1, 0].set_title('Ad Budget vs Sales')
axs[1, 0].set_xlabel('Ad Budget (₹)')
axs[1, 0].set_ylabel('Sales (₹)')

axs[1, 1].boxplot(df['Sales'])
axs[1, 1].set_title('Sales Boxplot')
axs[1, 1].set_ylabel('Sales (₹)')

plt.tight_layout()
plt.show()
