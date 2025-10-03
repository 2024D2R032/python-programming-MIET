correct = int(input("Enter Correct Answers: "))
wrong = int(input("Enter Wrong Answers: "))
unattempted = int(input("Enter Unattempted: "))

score = (correct * 4) + (wrong * -1)  # unattempted adds 0

print("Total Score:", score)

if score >= 180:
    print("Excellent")
elif score >= 120:
    print("Good")
elif score >= 60:
    print("Average")
else:
    print("Fail")

if wrong > correct:
    print("Improve accuracy!")
