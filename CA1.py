# Grocery Store Billing System
# Program to calculate total cost of 3 items with discount logic

# Accept price input for 3 items
item1 = float(input("Enter price of item 1: "))
item2 = float(input("Enter price of item 2: "))
item3 = float(input("Enter price of item 3: "))

# Calculate total cost
total_cost = item1 + item2 + item3

# Initialize discount
discount = 0

# Apply 10% discount if total exceeds $50
if total_cost > 50:
    discount = total_cost * 0.10

# Calculate final payable amount
final_amount = total_cost - discount

# Display results
print("\n--- Billing Summary ---")
print(f"Original Total: ${total_cost:.2f}")        #print Original Total Cost
print(f"Discount: ${discount:.2f}")                #print Discount (if any)   
print(f"Final Amount Payable: ${final_amount:.2f}")#print Final Amount to be paid




