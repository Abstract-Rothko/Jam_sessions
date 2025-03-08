# OOP Principals

# Classes and Objects

class Dog:
    species = "Canis Familiaris" # Class Attribute
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def speak(self):
        return f"{self.name} says, 'Woof!'"
        
buddy = Dog("Buddy", 3)
lucy = Dog("Lucy", 5)

print(buddy.speak()) # Output: Buddy says, 'Woof!'
print(lucy.species) # Output: Canis Familiaris

# Inheritance
class GoldenRetriever(Dog):
    def __init__(self, name, age, colour = "golden"):
        super().__init__(name, age)
        self.colour = colour
        
    def fetch(self, item):
        return f"{self.name} fetches {item}!"
        
    def speak(self):
        return f"{self.name} says Woof loudly!"
        
goldie = GoldenRetriever("Max", 2)
print(goldie.fetch("ball")) # Output: Max fetches ball!
print(goldie.speak()) # Output: Max says Woof loudly!

# Encapsulation
class BankAccount:
    def __init__(self, account_number, balance = 0):
        self._account_number = account_number # Protected Attribute
        self.__balance = balance # Private Attribute
        
    @property
    def balance(self):
        return self.__balance
        
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self.__balance = value
        else:
            print("Invalid Balance!")
            
            
account = BankAccount("12345", 1000)
account.balance = 1500 # Uses setter
print(account.balance) # Output: 1500
# account.__balance # AttributeError

# Polymorphism
class Cat:
    def speak(self):
        return "Meow!"
        
class Duck:
    def speak(self):
        return "Quack!"
        
        
def animal_speak(animal):
    print(animal.speak())
    
animals = [Dog("Zeke", 1), Cat(), Duck()]

for animal in animals:
    animal_speak(animal)
    
# Output:
# Zeke says, 'Woof!'
# Meow!
# Quack!

# Abstraction

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
        
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return round(pi * self.radius ** 2, 2)
        
class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return side ** 2
        
# shape = Shape() # Error: Cannot instantiate abstract class
circle = Circle(5)
print(circle.area()) # Output: 78.54

# Class vs Instance Attribute
class Employee:
    company = "Tech Corp" # class attribute
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
employee1 = Employee("Alice", 60_000)
employee2 = Employee("Bob", 65_000)

print(employee1.company) # Output: Tech Corp
Employee.company = "New Tech Corp"
print(employee2.company) # Output: New Tech Corp


# Special Methods
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"{self.title} by {self.author}"
        
    def __repr__(self):
        return f"Book(title={self.title}, author={self.author})"
        
        
book = Book("Python Basics", "John Doe")
print(book) # Output: Python Basics by John Doe
print(repr(book)) # Output: Book(title=Python Basics, author=John Doe)


# Composition
class Engine:
    def start(self):
        return "Engine started"
        
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.engine = Engine() # composition
        
    def drive(self):
        return self.engine.start() + f" - {self.make} {self.model} is moving."
        
        
my_car = Car("Generic", "Car")
print(my_car.drive()) # Output: Engine started - Generic Car is moving


# Static vs Class Methods

class TemperatureConverter:
    @staticmethod
    def celsius_to_farenheit(celsius):
        return celsius * (9/5) + 32
        
    @classmethod
    def from_farenheit(cls, farenheit):
        celsius = (farenheit - 32) * 5/9
        return cls(celsius)
        
    def __init__(self, celsius):
        self.celsius = celsius
        
print(TemperatureConverter.celsius_to_farenheit(30)) # Output: 86.0
temp = TemperatureConverter.from_farenheit(86)
print(temp.celsius) # Output: 30.0
    