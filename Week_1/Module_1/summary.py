"""
WAT WE LEARNED TODAY
1. Python setup
2. variable
3. operators
4. conditionals: if -elif -else
5. while
6. for
7. commenting
8. input
9. type casting
"""

""" 
HOMEWORK
1. float
2. take 3 numbers from the user and give me the largest number as output
3. take 3 numbers from the use and give me the sum of the numbers
4. run a loop and show my the odd numbers between 39 to 68
5. Grade calculator in python (if elif else)

"""

# 1. float
decimal_number = float(input("Enter a decimal number: "))
print("You entered:", decimal_number)

# 2. take 3 numbers from the user and give me the largest number as output
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))
print("The largest number is:", max(a, b, c))

# 3. take 3 numbers from the user and give me the sum of the numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
print("The sum of the numbers is:", num1 + num2 + num3)

# 4. run a loop and show me the odd numbers between 39 to 68
print("Odd numbers between 39 and 68:")
for i in range(39, 69):
    if i % 2 != 0:
        print(i, end=" ")
print()  # For newline

# 5. Grade calculator in python (if elif else)
score = float(input("Enter your score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print("Your grade is:", grade)
