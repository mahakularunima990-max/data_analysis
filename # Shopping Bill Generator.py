# Shopping Bill Generator

# Customer Details
customer_name = "Arunima Mahakul"
product_name = "Wireless Mouse"
quantity = 3
price_per_item = 500

# Calculations
subtotal = quantity * price_per_item
gst = subtotal * 0.18      # 18% GST
final_amount = subtotal + gst

# Print Invoice
print("=" * 45)
print("           SHOPPING BILL")
print("=" * 45)
print(f"Customer Name : {customer_name}")
print(f"Product Name  : {product_name}")
print(f"Quantity      : {quantity}")
print(f"Price/Item    : ₹{price_per_item:.2f}")
print("-" * 45)
print(f"Subtotal      : ₹{subtotal:.2f}")
print(f"GST (18%)     : ₹{gst:.2f}")
print("-" * 45)
print(f"Final Amount  : ₹{final_amount:.2f}")
print("=" * 45)
print("      Thank You for Shopping!")
print("=" * 45)