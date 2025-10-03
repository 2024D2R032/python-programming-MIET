balance = float(input("Enter Account Balance: "))
withdraw = float(input("Enter Amount to Withdraw: "))
acc_type = input("Enter Account Type (Saving/Current): ").lower()
day = input("Enter Day (weekday/weekend): ").lower()

fee = 50 if day == "weekend" else 0
limit = 25000 if acc_type == "saving" else 50000


if withdraw > limit:
    print("Failure: Withdrawal exceeds daily limit")
elif balance < withdraw + 1000 + fee:
    print("Failure: Insufficient balance (must keep ₹1000 minimum)")
else:
    balance -= (withdraw + fee)
    print("Success: Withdrawal Completed")
    print("Updated Balance = ₹", balance)
