import matplotlib.pyplot as plt

months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
]
sales = [
    45000,
    52000,
    48000,
    61000,
    58000,
    65000,
    62000,
    70000,
    68000,
    75000,
    72000,
    80000,
]
max_sales = max(sales)
min_sales = min(sales)
max_month = months[sales.index(max_sales)]
min_month = months[sales.index(min_sales)]

print(f"Highest Sales: {max_month} with ₹{max_sales}")
print(f"Lowest Sales: {min_month} with ₹{min_sales}")

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(months, sales, marker="o", color="b", linestyle="-")
plt.title("Monthly Sales Revenue (Line Chart)")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.bar(months, sales, color="orange")
plt.title("Monthly Sales Revenue (Bar Chart)")
plt.xlabel("Month")
plt.ylabel("Sales (₹)")

plt.tight_layout()
plt.show()
