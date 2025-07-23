# Task 1(Write a program that takes two numbers as inputs from the user and prints their sum)
number_1 = float(input("Enter first number:"))
number_2= float(input("Enter second number:"))
print("Sum:", number_1 + number_2)#simple calculator 

# Task 2(Write a program that takes an integer input from the user. Use a for loop to print all numbers from that integer down to 0)
n = int(input("Enter an integer:"))
for i in range(n, -1, -1):
    print(i) #will countdown

# Task 3(Write a program that takes an integer input from the user. Use a while loop to keep doubling the number until it is greater than 1000, then print the result)
n = int(input("Enter an integer:"))
while n <= 1000:#will double the nuber untell reach 1000 
    n *= 2
print("Result after doubling:", n) 

# Task 3(Write a function that takes a number as input and returns the square of the number. Use it in a program that takes an input from the user and prints the square)
def square(numbersquared):
    return numbersquared ** 2

n = float(input("Enter a number u want to squar it:\n"))
print(square(n))#will sequar the nuber u enterd

# Task 5 ( Write a program that takes a number as input from the user. If the number is greater than 10, print "Big number". If the number is less than or equal to 10, print "Small number")
num = float(input("Enter a number:"))
if num > 10:
    print("Big number")
else:
    print("Small number")

# Task 6 (Write a function that takes two numbers as inputs and returns their product. Use this function in a program that takes two inputs from the user and prints the product)
def multiply(x, y):
    return x * y

ur_number1 = float(input("Enter first number:"))
ur_number2 = float(input("Enter second number:"))
print("Product:", multiply(ur_number1, ur_number2))

# Task 7 (Write a program that uses a while loop to take a number as input from the user, subtract 5, and print the result. Continue this until the result is less than 0)
number_subtracted = float(input("Enter a number:"))
while number_subtracted >= 0:
    number_subtracted -= 5
    print("number after got subtract:", number_subtracted)

# Task 8 (Write a program that uses a for loop to take an integer input from the user and print the factorial of that number)
numberfactorialed = int(input("Enter an integer:"))
factorial = 1
for i in range(1, numberfactorialed + 1):
    factorial *= i
print("number after got Factorialed:", factorial)

# Task 9 (Write a program that takes a number as input from the user. If the number is positive, print "Positive". If the number is negative, print "Negative". If the number is zero, print "Zero")
n1 = float(input("Enter a number:"))
if n1 > 0:
    print("Positive")
elif n1 < 0:
    print("Negative")
else:
    print("Zero")

# Task 10 (Write a lambda function that takes two numbers as inputs and returns their division as a floating-point number. Use this function in a program that takes two inputs from the user and prints the division)
divide = lambda a, b: float(a) / float(b)

a = float(input("Enter numerator: "))
b = float(input("Enter denominator: "))
if b != 0:
    print("Division result:", divide(a, b))
else:
    print("Cannot divide by zero.")