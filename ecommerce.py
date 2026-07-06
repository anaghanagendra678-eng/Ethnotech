import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset (Excel file)
data = pd.read_excel("Online Retail.xlsx")

# Show columns and sample data
print("Columns:", data.columns)
print(data.head())

# Drop rows with missing CustomerID
data = data.dropna(subset=['CustomerID'])

# Calculate total revenue per transaction
data['Revenue'] = data['Quantity'] * data['UnitPrice']

# -------------------------------
# Top 10 customers by total revenue
# -------------------------------
top_customers = data.groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Customers by Revenue:")
print(top_customers)

# -------------------------------
# Total revenue over time (monthly)
# -------------------------------
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
monthly_revenue = data.groupby(data['InvoiceDate'].dt.to_period('M'))['Revenue'].sum()

plt.figure(figsize=(12,6))
monthly_revenue.plot(marker='o')
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.show()

# -------------------------------
# Top 10 products by quantity sold
# -------------------------------
top_products = data.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Quantity Sold:")
print(top_products)

# Convert to DataFrame for Seaborn plotting
top_products_df = top_products.reset_index()
top_products_df.columns = ['Product', 'Quantity']

# Plot top 10 products with Seaborn
plt.figure(figsize=(12,6))
sns.barplot(
    x='Quantity', 
    y='Product', 
    data=top_products_df, 
    palette="viridis", 
    hue='Product',  # assign hue for Seaborn >=0.14
    dodge=False
)
plt.legend([],[], frameon=False)  # Hide legend
plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Quantity Sold")
plt.ylabel("Product")
plt.show()
