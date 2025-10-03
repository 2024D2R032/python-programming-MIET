speed = int(input("Enter Speed: "))
vehicle = input("Enter Vehicle Type (car/bike/truck): ").lower()
seat_belt = input("Seat Belt Worn? (Yes/No): ").lower()
helmet = input("Helmet Worn? (Yes/No): ").lower() if vehicle == "bike" else "yes"

fine = 0

if speed > 80:
    fine += 2000
if vehicle == "car" and seat_belt == "no":
    fine += 1000
if vehicle == "bike" and helmet == "no":
    fine += 1500
if vehicle == "truck" and speed > 60:
    fine += 3000

if fine == 0:
    print("No Fine. Drive Safe 🚗")
else:
    print("Total Fine = ₹", fine)
