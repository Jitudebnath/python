"""Sales related problem"""

import numpy as np
import matplotlib.pyplot as plt

sales_data = np.array(
    [
        [1, 150000, 180000, 220000, 250000],  # Paradise Biryani
        [2, 350000, 420000, 520000, 640000],  # Beijing Bites
        [3, 850000, 120000, 820000, 650000],  # Pizza Hub
        [4, 950000, 420000, 620000, 630000],  # Burger point
        [5, 650000, 820000, 920000, 670000],  # Chai point
    ]
)
print("==Zomato sales analysis==")
print("\n sales data shpae", sales_data.shape)
print("\n Sample data for 1st 3 resturant:", sales_data[:, 1:])

yearly_total = np.sum(sales_data[:, 1:], axis=0)
print("Yearly_total collection:", yearly_total)

# minimum sale
min_sales = np.min(sales_data[:, 1:], axis=1)
print("minimum sales :", min_sales)

# Maximum sale
max_sales = np.max(sales_data[:, 1:], axis=0)
print("maximum sales:", max_sales)

# Average sales per resturant
avg_sales = np.mean(sales_data[:, 1:], axis=1)
print("Average sales:", avg_sales)

cumsum = np.mean(sales_data[:, 1:], axis=1)
print(cumsum)
plt.figure(figsize=(10, 6))
plt.plot(np.mean(cumsum, axis=0))
plt.title("Average cumulative sales accross all resturant")
plt.xlabel("Years")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
