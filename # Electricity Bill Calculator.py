# Electricity Bill Calculator

# Customer Details
customer_name = "Arunima Mahakul"
units_consumed = 250
cost_per_unit = 8

# Calculations
total_bill = units_consumed * cost_per_unit
electricity_tax = total_bill * 0.08    # 8% Electricity Tax
final_bill = total_bill + electricity_tax

# Print Electricity Bill
print("=" * 45)
print("         ELECTRICITY BILL")
print("=" * 45)
print(f"Customer Name      : {customer_name}")
print(f"Units Consumed     : {units_consumed}")
print(f"Cost Per Unit      : ₹{cost_per_unit:.2f}")
print("-" * 45)
print(f"Total Bill         : ₹{total_bill:.2f}")
print(f"Electricity Tax(8%): ₹{electricity_tax:.2f}")
print("-" * 45)
print(f"Final Bill         : ₹{final_bill:.2f}")
print("=" * 45)
print("      Thank You! Pay on Time.")
print("=" * 45)