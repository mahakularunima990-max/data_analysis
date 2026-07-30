# Restaurant Bill Calculator

# Customer Details
customer_name = "Arunima Mahakul"
food_bill = 1200

# Calculations
gst = food_bill * 0.05          # 5% GST
service_charge = food_bill * 0.10   # 10% Service Charge

final_amount = food_bill + gst + service_charge

# Print Restaurant Bill
print("=" * 45)
print("         RESTAURANT BILL")
print("=" * 45)
print(f"Customer Name   : {customer_name}")
print("-" * 45)
print(f"Food Bill       : ₹{food_bill:.2f}")
print(f"GST (5%)        : ₹{gst:.2f}")
print(f"Service Charge  : ₹{service_charge:.2f}")
print("-" * 45)
print(f"Final Amount    : ₹{final_amount:.2f}")
print("=" * 45)
print("      Thank You! Visit Again.")
print("=" * 45)