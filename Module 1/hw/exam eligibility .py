# Program to calculate attendance percentage

# Input from user
working_days = int(input("Enter total working days: "))
absent_days = int(input("Enter total absent days: "))

# Calculate attended days
attended_days = working_days - absent_days

# Calculate percentage
percentage = (attended_days / working_days) * 100

# Display percentage
print("Attendance Percentage =", percentage, "%")

# Check eligibility
if percentage < 75/100:
    print("Student is NOT allowed to sit in the exam.")
else:
    print("Student is allowed to sit in the exam.")