
# PYTHON BASICS
# Summary: 
# Understand Python syntax, variables, data types, and basic I/O operations.

# Example:

# Declaring variables
name = "Adam"
age = 22
print(f"My name is {name} and I am {age} years old.")

# Practice Questions:

# 1. Write a program to accept user input and print it in uppercase.

def uppercase():
    response = input("Enter input: ")
    print(response.upper())

# 2. Calculate the area of a rectangle given its length and width.

rec_length = 10
rec_width = 5.4

area = rec_length * rec_width
print(area)

# 3. Swap two variables without using a third variable.

var_1 = "Chris Brown"
var_2 = "Lil Dicky"

var_1, var_2 = var_2, var_1

# CONTROL FLOW
# Summary:
# Learn to use if statements, for loops, and while loops to control the flow of the program.

#Example:

# Check if a number is even or odd
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Practice Questions:

# 1. Write a program to find the largest of three numbers.

a = 12
b = 13
c = 8

if a > b and a > c:
    print(f"The largest number: {a}")
elif b > a and b > c:
    print(f"The largest number: {b}")
else:
    print(f"The largest number: {c}")


# 2. Use a for loop to print the Fibonacci series up to 10 terms.

def fibonacci_sequence(n):
    sequence = [1]
    previous = 0
    current = 1
    for _ in range(n):
        new = previous + current
        sequence.append(new)
        previous = current
        current = new
    return sequence

#3. Create a while loop that prints numbers from 1 to 10.

n = 1
while n <= 10:
    print(n)
    n += 1
    
# FUNCTIONS
# Summary: 
# Master defining, calling, and using functions to modularize your code.

#Example:

def greet(name):
    return f"Hello, {name}!"

print(greet("Adam"))

# Practice Questions:

# 1. Write a function to check if a number is prime.

def is_prime(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    if len(factors) == 2:
        return True
    else:
        return False

print(is_prime(5)) # True
print(is_prime(8)) # False

# 2. Create a function that takes a list of numbers and returns their average.

def average(number_list):
    total = 0
    for i in number_list:
        total += i
    length = len(number_list)
    avg = round(total / length, 2)
    return avg

print(average([8, 11, 13, 18, 20, 22, 42])) #19.14

#3. Write a recursive function to calculate the factorial of a number.

def factorial(n):
    if n < 2:
        return n
    else:
        return n * factorial(n - 1) 

print(factorial(10)) # 3628800

# DATA STRUCTURES
# Summary: 
# Learn to manipulate and use Python’s built-in data structures.

# Example:

# Using a dictionary
phone_book = {"Adam": 00001, "Eve": 00002}
print(phone_book["Adam"])

# Practice Questions:

# 1. Write a program to find the maximum and minimum values in a list.

lst = [10, 12, 13, 45, 23, 67, 0]
largest = lst[0]
smallest = lst[0]
for i in lst:
    if i > largest:
        largest = i

for i in lst:
    if i < smallest:
        smallest = i        
print(largest) # 67
print(smallest) # 0

# 2. Use a dictionary to count the occurrences of characters in a string.

string = "The Weeknd"

def mapping(strings):
    dictionary = {}
    unique = ""
    for string in strings:
        if string not in unique and string != " ":
            unique += string
            
    for i in unique:
        dictionary[i] = strings.count(i)
        
    return dictionary

print(mapping("The Weeknd")) # {'T': 1, 'h': 1, 'e': 3, 'W': 1, 'k': 1, 'n': 1, 'd': 1}

# 3. Create a set of unique elements from a list.

list_of_numbers = fibonacci_sequence(15)
print(set(list_of_numbers)) # {1, 2, 3, 34, 5, 610, 8, 233, 377, 13, 144, 21, 55, 89, 987}

# OBJECT-ORIENTED PROGRAMMING (OOP)
# Summary: 
# Learn to design and use classes, objects, inheritance, and encapsulation.

#Example:

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

cat = Animal("Cat")
print(cat.speak())

#Practice Questions:

# 1. Create a class for a car with attributes like make, model, and year.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self._state = False
        
    def __str__(self):
        return f"This is a {self.make} {self.model} from the year {self.year}."
    
    def __repr__(self):
        return f"Car(make = {self.make}, model = {self.model}, year = {self.year})"
        
    def drive(self, speed):
        if self._state == False:
            print(f"The car is driving at {speed} kilometres per hour.")
            self.state == True
        else:
            print("This car is already driving!")
            
    def stop(self):
        if self._state == True:
            print("The car has come to a stop.")
        else:
            print("The car has already stopped.")
            

car = Car("Audi", "R8", 2016)
car.drive(120)

# 2. Implement inheritance where a Dog class inherits from an Animal class.

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
        
    def bark(self):
        return "Woof!"

    def walk(self):
        return f"{self.name} goes for a walk with you."

dog = Dog("Snoop Dogg", "Long Beach")
print(dog.speak()) # Snoop Dogg makes a sound.

# 3. Use a private attribute in a class and write methods to access it.

class Incarnation:
    def __init__(self, name, age, role, skills):
        self.name = name
        self.age = age
        self.role = role
        self.skills = skills
        self.__hp = 100
        
    def sacrificial_skill(self):
        print(f"{self.name} uses sacrificial skill. 10 hp will be removed from your life.")
        self.__hp -= 10
        
    def training(self):
        print(f"{self.name} undergoes private training. 15 hp will be given to your life.")
        self.__hp += 15
        
MF_DOOM = Incarnation("Zev Luv X", 2004, "Mad Villain", ["Quirky Lyricism", "Complex Rhyme Schemes", "Unique Production"])
MF_DOOM.sacrificial_skill() # Zev Luv X uses sacrificial skill. 10 hp will be removed from your life.
print(MF_DOOM._Incarnation__hp) # 90

# FILE HANDLING
# Summary: Learn to read from and write to files.

# Example:
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, world!")

# Practice Questions:

# 1. Write a program to read a file and count the number of words.

path = "../test_folder/Test.txt"

try:
    file = open(path, "rt", encoding = 'utf-8')
    text = file.read()
    print(text)
    words = text.split()
    print("Word Count: ", len(words))
    file.close()
except Exception as exc:
    print("File could not be opened: ", exc)

# 2. Create a program to append text to an existing file.

try:
    file = open(path, "a", encoding = "utf-8")
    file.write("\nRothko, the certified greatest, was here.\n")
    print("Task Executed") # Confirmation that it did work
except Exception as e:
    print("File could not be properly handled: ", e)
finally:
    file.close()

# 3. Write a program to find the longest word in a text file.

def longest_word(iterable):
    count = 0
    longest_word = ""
    for i in iterable:
        if len(i) > count:
            count = len(i)
            longest_word = i
    return longest_word

try:
    file = open(path, "rt", encoding = "utf-8")
    text = file.read().split()
    print("The longest word is: ", longest_word(text))
except Exception as e:
    print("File could not be opened: ", e)
finally:
    file.close()

# ERROR AND EXCEPTION HANDLING
# Summary: 
# Understand how to handle runtime errors gracefully using try, except, and finally.

# Example:

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Practice Questions:

# 1. Write a program to catch and handle a FileNotFoundError.

try:
    file = open("test_file.txt", "rt")
except FileNotFoundError:
    print("No file found.")


# 2. Create a custom exception for invalid age input (e.g., age cannot be negative).

class AgeError(Exception):
    pass
    
def age():
    age = int(input("Enter your age: "))
    if age < 0:
        raise AgeError("Age cannot be negative.")
    else:
        print(age)
        
age() # Enter -1, AgeError was raised.


# 3. Use finally to ensure a file is closed after being opened.

path = "../text.txt"

try:
    file = open(path, "rt", encoding = "utf-8")
    print("File opened.")
    text = file.read()
    print(text)
except Exeption as e:
    print("File could not be opened: ", e)
finally:
    file.close()
    print("File closed.")

# MODULES AND LIBRARIES
# Summary: 
# Learn to import and use built-in and third-party libraries.

#Example:

import math

print(math.sqrt(16))

# Practice Questions:

# 1. Write a program to generate random numbers using the random module.

from random import choices

generated_list = choices(range(100), k = 30)

print(generated_list)


# 2. Use the datetime module to print the current date and time.

from datetime import datetime

print(datetime.now())

# ITERATORS AND GENERATORS
# Summary: 
# Master iterators for looping and generators for memory-efficient programming.

# Example:

def generate_numbers():
    for i in range(5):
        yield i

for num in generate_numbers():
    print(num)

# Practice Questions:

# 1. Write a generator function to produce even numbers up to a given limit.

def generate_numbers(n = 10):
    for i in range(0, n + 1, 2):
        yield i

numbers = [x for x in generate_numbers(100)]

# 2. Create a custom iterator for looping over a string backward.

string = "Jesus Piece."

for i in string[::-1]:
    print(i)