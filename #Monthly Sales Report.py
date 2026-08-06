#Monthly Sales Report
import numpy as np
monthly_sales = np.array([1200, 1500, 1700, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000])
# Calculate total sales
total_sales = np.sum(monthly_sales)
# Calculate average sales
average_sales = np.mean(monthly_sales)
# Calculate maximum sales
max_sales = np.max(monthly_sales)
# Calculate minimum sales
min_sales = np.min(monthly_sales)
# Print the results
print("Monthly Sales Report")
print("---------------------")
print(f"Total Sales: ₹{total_sales}")
print(f"Average Sales: ₹{average_sales:.2f}")   
print(f"Maximum Sales: ₹{max_sales}")
print(f"Minimum Sales: ₹{min_sales}")
