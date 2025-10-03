## Writea program to accept marksof 5 subjects from user calculate total,calculate percentage , print result pass or fail on the basis of percentage 
## percentage greater than or equal to 50 : pass otherwise fail
# Accept marks for 5 subjects from the user
subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))
subject4 = float(input("Enter marks for Subject 4: "))
subject5 = float(input("Enter marks for Subject 5: "))

# Calculate total marks
total = subject1 + subject2 + subject3 + subject4 + subject5

# Calculate percentage
percentage = total / 5

# Display total and percentage
print("\nTotal Marks:", total)
print("Percentage:", percentage, "%")

# Determine pass or fail
if percentage >= 50:
    print("Result: PASS ")
else:
    print("Result: FAIL ")
