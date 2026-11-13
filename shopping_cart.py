
customer_name = input("Customer Name: ")

p1_name = input("Enter Product1 Name: ")
p1_price = float(input("Price: "))

p2_name = input("Enter Product2 Name: ")
p2_price = float(input("Price: "))

p3_name = input("Enter Product3 Name: ")
p3_price = float(input("Price: "))

# Calculate Subtotal
subtotal = p1_price + p2_price + p3_price

#  Determine the discount rate 
if subtotal >= 5000:
    discount_rate = 0.20
elif subtotal >= 3000:
    discount_rate = 0.10
elif subtotal >= 1000:
    discount_rate = 0.05
else:
    discount_rate = 0.00

# Calculate Discount and Final Total
discount = subtotal * discount_rate
final_total = subtotal - discount

# Display the shopping summary 

print("\n--- Shopping Summary ---")
print(f"Customer Name: {customer_name}")
print(f"Product 1: {p1_name}")
print(f"Price: {p1_price}")
print(f"Product 2: {p2_name}")
print(f"Price: {p2_price}")
print(f"Product 3: {p3_name}")
print(f"Price: {p3_price}")
print(f"Subtotal: {subtotal}")
print(f"Discount: {discount}")
print(f"Final Total: {final_total}")