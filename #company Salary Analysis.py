#company Salary Analysis
import numpy as np
salaries = np.array([50000, 60000, 70000, 80000, 90000, 100000, 110000, 120000, 130000, 140000])
# Calculate average salary
average_salary = np.mean(salaries)
# Calculate maximum salary
max_salary = np.max(salaries)
# Calculate minimum salary
min_salary = np.min(salaries)
# Print the results
print("Company Salary Analysis")
print("-----------------------")
print(f"Salarys: {salaries}")
print(f"Average Salary: ₹{average_salary:.2f}")   
print(f"Highest Salary: ₹{max_salary}")
print(f"Lowest Salary: ₹{min_salary}")