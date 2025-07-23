#Task 1:
'''Create a parent class `Shape` with a method `area` that returns 0. Then, create two child classes,
`Rectangle` and `Circle`. `Rectangle` has attributes `width` and `height`, `Circle` has an attribute `radius`.
Override the `area` method in both child classes to calculate the area correctly (use 3.14 as an approximation for pi)'''

class My_Shape:
    def area(self):
        return 0
    
    def print_info(self):
        print(type(My_Shape))
        print(f"The Area Is: {self.area()}")

class Rectangle(My_Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height
    
    def print_info(self):
        print(type(My_Shape))
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")
        print(f"Area: {self.area()}")

class Circle(My_Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
    def print_info(self):
        print(type(My_Shape))
        print(f"Radius: {self.radius}")
        print(f"Area: {self.area()}")


Ur_Rectangle = Rectangle(10, 6)
print("Ur Rectangle Area Is:", Ur_Rectangle.area())

Ur_Circle = Circle(9)
print("Ur Circle Area Is:", Ur_Circle.area())

####################################################

#Task 2:
'''Expand on the previous task. Add a method `print_info` to the `Shape` class that prints out the type of shape and its area.
For each child class, override this method to print the shape type (rectangle or circle),
its specific attributes (width and height for rectangles, radius for circles), and its area.'''

rectangle = Rectangle(5, 3)
rectangle.print_info()

print()

circle = Circle(4)
circle.print_info()

#####################################################

#Task 3:
'''Create a class `BankAccount` with private attributes `__account_number` and `__balance`.
Provide getter methods for both (get_account_number, get_balance), and methods to deposit and withdraw money.
Ensure that the `withdraw` method checks if there is enough balance before withdrawing.'''

class BankAcc:
    def __init__(self,account_number, balance, ur_balance = 0):
        self._account_number = account_number
        self._balance = balance
    
    def get_account_number(self):
        return self._account_number
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance is {self._balance}")
        else:
            print("error") 
    
    def withdraw(self, amount):
        if amount > self._balance:
            print("u don't have money")
        elif amount <= 0:
            print("error")
        else:
            self._balance -= amount
            print(f"Withdrew {amount}. New balance is {self._balance}")

account = BankAcc("80973459", 50000)

print("Account Number:", account.get_account_number())
print("Balance:", account.get_balance())

account.deposit(95)
account.withdraw(225)
account.withdraw(900)
account.deposit(500)

#########################################################

#Task 4:
'''Create a base class `Animal` that has a method `speak()` which prints `"I don't know what I say!"`.
Then create two derived classes `Dog` and `Cat` which override the `speak()` method.
The `speak()` method in the `Dog` class should print `"Woof Woof!"` and the `speak()` method in the `Cat` class should print `"Meow Meow!"`'''

class My_Animal:
    def speak(self):
        print("I don't know what I say!")
    
class My_Dog(My_Animal):
    def speak(self):
        print("Woof Woof!")

class My_Cat(My_Animal):
    def speak(self):
        print("Meow Meow!")

animal = My_Animal()
dog = My_Dog()
cat = My_Cat()

animal.speak()
dog.speak()     
cat.speak()

########################################################

#Task 5:
'''Continuing from the above task, create a function `animal_speak(animal)` which accepts an `Animal` object and calls its `speak()` method.
This demonstrates polymorphism because you can pass any object of a class derived from `Animal` to this function and it will work'''

def animal_speak(animal):
    animal.speak()

animal_speak(animal)

########################################################

#Task 6:
'''Create a class `Car` with two attributes: `color` (public) and `__speed` (private).
The class should have methods `accelerate()` which increases the speed by 10 and `get_speed()` which returns the current speed.
The `__speed` attribute should be modified only through the `accelerate()` method, demonstrating the principle of encapsulation.'''

class Car:
    def __init__(self, color):
        self.color = color       
        self.__speed = 0         

    def accelerate(self):
        self.__speed += 10       

    def get_speed(self):
        return self.__speed

My_car = Car("Red")
print("Ur Car Color Is:", My_car.color)
print("Ur Car Speed:", My_car.get_speed())

for i in range(20):
    My_car.accelerate() #this thing here meant to be an a joke but it works XDDDDD

print("Speed after 20 accelerate:", My_car.get_speed())

