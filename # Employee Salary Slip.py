# Employee Salary Slip

# Employee Details
employee_name = "Arunima Mahakul"
employee_id = "EMP101"
basic_salary = 50000

# Salary Calculations
hra = basic_salary * 0.20      # 20% HRA
da = basic_salary * 0.15       # 15% DA
pf = basic_salary * 0.12       # 12% PF

gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf

# Print Salary Slip
print("=" * 40)
print("          EMPLOYEE SALARY SLIP")
print("=" * 40)
print(f"Employee Name : {employee_name}")
print(f"Employee ID   : {employee_id}")
print("-" * 40)
print(f"Basic Salary  : ₹{basic_salary:.2f}")
print(f"HRA (20%)     : ₹{hra:.2f}")
print(f"DA (15%)      : ₹{da:.2f}")
print(f"PF (12%)      : ₹{pf:.2f}")
print("-" * 40)
print(f"Gross Salary  : ₹{gross_salary:.2f}")
print(f"Net Salary    : ₹{net_salary:.2f}")
print("=" * 40)
print("      Thank You!")
print("=" * 40)