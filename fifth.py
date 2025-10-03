## Program to accept price of10 different items from user, calculate total amount 
## provide discount on the basis of amount ,if amount exceed 2000 applied discount 20% ,display discount and final amount otherwise no discount

# Initialize an empty list to store item prices
item_prices = []

# Accept prices for 10 items
for i in range(1, 11):
    price = float(input(f"Enter price of item {i}: ₹"))
    item_prices.append(price)

# Calculate total amount
total_amount = sum(item_prices)

# Check for discount eligibility
if total_amount > 2000:
    discount = total_amount * 0.20
    final_amount = total_amount - discount
    print("\n🎉 Discount Applied: ₹", round(discount, 2))
else:
    discount = 0
    final_amount = total_amount
    print("\nNo discount applied.")

# Display final results
print(" Total Amount: ₹", round(total_amount, 2))
print("Final Amount to Pay: ₹", round(final_amount, 2))
