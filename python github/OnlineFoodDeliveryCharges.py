distance = float(input("Enter Distance (in km): "))
order = float(input("Enter Order Amount: "))
user = input("Enter User Type (Normal/Gold/Platinum): ").lower()

# Membership discount
if user == "gold":
    order *= 0.8   # 20% off
elif user == "platinum":
    order *= 0.7   # 30% off

# Delivery charges
if order >= 1000:
    delivery = 0
else:
    delivery = 50
    if distance > 5:
        delivery += (distance - 5) * 10

final_bill = order + delivery

print("Final Bill Amount = ₹", final_bill)
