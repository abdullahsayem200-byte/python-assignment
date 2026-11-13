
# Student Grade Calculator

name = input("Enter student's name: ")

mark1 = float(input("Enter marks for English: "))
mark2 = float(input("Enter marks for Mathmetics: "))
mark3 = float(input("Enter marks for Pyhton: "))

# Calculate total and average
total = mark1 + mark2 + mark3
average = total / 3

# Determine grade
if average >= 80:
    grade = "A+"
elif average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "F"

# Display the result using f-string
print("\n----- Student Result -----")
print(f"Student Name: {name}")
print(f"Total Marks: {total:.0f}")
print(f"Average: {average:.2f}")
print(f"Grade: {grade}")
