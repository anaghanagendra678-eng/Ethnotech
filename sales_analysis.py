import pandas as pd
import matplotlib.pyplot as plt

# Load tables with proper encoding
orders = pd.read_csv("orders.csv", encoding='latin1')
order_details = pd.read_csv("order_details.csv", encoding='latin1')
pizzas = pd.read_csv("pizzas.csv", encoding='latin1')
pizza_types = pd.read_csv("pizza_types.csv", encoding='latin1')

# Continue with merging and analysis...

# Merge order details with pizza info
details = pd.merge(order_details, pizzas, on="pizza_id")
details = pd.merge(details, pizza_types, on="pizza_type_id")

# Combine with orders to get datetime
orders["date"] = pd.to_datetime(orders["date"])
data = pd.merge(details, orders, on="order_id")

# Add revenue column
data["revenue"] = data["quantity"] * data["price"]

# Total yearly revenue
total_revenue = data["revenue"].sum()
print("Total Revenue: $", total_revenue)

# Best selling pizzas by quantity
best_selling = data.groupby("name")["quantity"].sum().sort_values(ascending=False)
print("\nTop Selling Pizzas:\n", best_selling.head(10))

# Most revenue generating pizzas
top_revenue = data.groupby("name")["revenue"].sum().sort_values(ascending=False)
print("\nTop Revenue Pizzas:\n", top_revenue.head(10))

# Extract hour from 24-hour time column
data["hour"] = pd.to_datetime(data["time"], format='%H:%M:%S').dt.hour

# Revenue by hour
hourly = data.groupby("hour")["revenue"].sum()

# Plot
plt.figure(figsize=(10,5))
hourly.plot(marker="o")
plt.title("Revenue by Hour of Day")
plt.xlabel("Hour")
plt.ylabel("Revenue")
plt.show()
