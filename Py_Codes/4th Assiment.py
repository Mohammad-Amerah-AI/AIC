#Task 1:
'''You have a list of numbers and you want to check if each number is in another list called special_numbers.

If the number is in the list, print the number; otherwise, print "Not in special numbers".

list1=[1,2,3,4]

list2=[1,4,5,6]
'''
list1=[1,2,3,4]
special_numbers=[1,4,5,6]
for num in special_numbers:
    if num in list1:
        print(num)
    else:
        print("not a special number")

###############################################################

#Task 2:
'''You have the following list_chars = ['A', 'B', 'C']
I want you to write a Python program to get this result'''

#what kide of result u want me to give u????!!!!!!

################################################################

#Tsak 3: (Print all numbers from 0 to 10 using a while loop)

number =1
while number < 10:
    print(number)
    number = number + 1    
print(number)

################################################################

#Task 4: (Write a function that prints your name (without any parameters)

def my_name():
    Name = input("what  should I call u ?!")
    print(f"Call Me {Name}")
my_name()

################################################################

#Task 5:
'''Write a function with two parameters (first_name , last_name) and then print (my full name is {first_name} , {last_name})'''

def my_name(First_Name,Last_Name):
    First_Name = input("what is ur first name ?!")
    Last_Name = input("what is ur last name ?!")
    print(f"My Full Name Is {First_Name},{Last_Name}")

my_name('mohammad', 'Amerah')

################################################################

#Task 6:
'''Write a function that takes two numbers a and b and assign b to a default value 5 and then print(a + b)'''

def sumnation(a,b=5):
    print(a+b)
sumnation(1,6)

#################################################################

#Task 7:
'''Create a function takes a list of numbers and prints whether each number is even or odd'''

def even_odd(numbers):
    for i in numbers:
        if i % 2 == 0:
            print(f"this number {i} is even")
        else:
            print(f"this number {i} is odd")
        
even_odd([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22])

