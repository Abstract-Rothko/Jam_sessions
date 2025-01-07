# List of practice functions

from datetime import datetime
import time

CURRENT_YEAR = datetime.today().year
GREGORIAN_CALENDAR_START = 1582

def is_leap_year():
    """
    This function determines if the input year is a leap year or not.
    
    >> is_leap_year() # Enter a year: 2016
    
    > 2016 is a leap year.
    """
    year = int(input("Enter a year: "))
    if year >= GREGORIAN_CALENDAR_START and year <= CURRENT_YEAR:
        leap_year = False
        if year % 4 == 0:
            leap_year = True
            
        if year % 100 == 0:
            leap_year = False
            
        if year % 400 == 0:
            leap_year = True
            
        if leap_year:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    elif year > CURRENT_YEAR:
        print(f"{year} is in the future. Pick a different year.")
    else:
        print(f"{year} is not within Gregorian Calendar")


def fun():
    """
    In this function, any number that you enter will undergo a number steps to reach the number. 
    
    (Note: There is a name for this formula, but I can't remember)
    
    >> fun()
        Enter a number: 32
    
    > 16
        8
        4
        2
        1
        steps =  5
    """
    number = int(input("Enter a number: "))
    steps = 0
    while number != 1:
        if number % 2 == 0:
            number = int(number / 2)
            steps += 1
            time.sleep(.5)
            print(number)
        else:
            number = int((3 * number) + 1)
            steps += 1
            time.sleep(.5)
            print(c0)
            
    time.sleep(1)
    print("steps = ", steps)
    

def event_end_time():
    """
    This function determines the ending time of an event once the starting hour, starting minutes and duration(in minutes) are given.
    
    >> event_end_time()
    Starting time(hours): 07
    Starting time(mins): 30
    Event duration(minutes): 250
    
    > 11:40
    """
    hour = int(input("Starting time(hours): "))
    mins = int(input("Starting time(mins): "))
    duration = int(input("Event duration(minutes): "))
    mins += duration
    hour += mins // 60
    mins %=  60
    hour %= 24
    print(hour, ":", mins, sep = '')
    
    
def personal_income_tax():
    """
    This function calculates how much tax someone would need to pay — in a fictional setting, of course.
    
    >> personal_income_tax()
    Enter Annual Income: 100000
    
    > Your income tax is R19374.04

    """
    annual_income = float(input("Enter Annual Income: "))
    if annual_income < 85_528:
        tax = (annual_income * .18) - 556.02
        print(f"Your income tax is R{tax:.2f}")
    else:
        tax = (annual_income - 85_828) * .32 + 14_839
        print(f"Your income tax is R{tax:.2f}")
   
        
def pyramid_height():
    """
    This function returns number layers a 2D pyramid would make if you input the total blocks used.
    
    >> pyramid_height()
    Enter total blocks used: 300

    The height of a pyramid: 24

    """
    blocks = int(input("Enter total blocks used: "))
    counter = 1
    layers = 0
    while blocks > 0:
        counter += 1
        layers += 1
        blocks -= counter
    print("The height of a pyramid:", layers)


        
def sort_list(data, swapped = True):
    """
    This fiction sorts any list of numbers in ascending order.
    
    :param data: list of unordered values(expected to be a list of numbers)
    :param swapped: iniates the function to enter a loop(expected to be a boolean)
    :return: list of ordered values(expected to be a list of numbers)
    
    >> print(sort_list([12, 45, 13, 56, 37, 3, 87, 88, 88, 99]))
    
    > [3, 12, 13, 37, 45, 56, 87, 88, 88, 99]
    
    """
    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                swapped = True
                data[i], data[i + 1] = data[i + 1], data[i]
    return data
    
    
def bmi_calculator(weight, height):
    """
    Calculates the bmi of the arguments entered.
    
    :param weight: expected to be a float
    :param height: expected to be a float
    :return: bmi value(expected to be a float)
    
    >> print(bmi_calculator(58, 1.78))
    
    > 18.31
    
    """
    if height < 1.0 or height > 2.5:
        return None
    if weight < 20 or weight > 200:
        return None
    return round(weight / height ** 2, 2)
    
    
def is_a_triangle(a, b, c):
    """
    Determines if the three given lengths could create a triangle.
    
    :param a: length of one side(expected to be an integer)
    :param b: length of one side(expected to be an integer)
    :param c: length of one side(expected to be an integer)
    
    """
    return a + b > c and b + c > a and c + a > b
    
    
def is_a_right_triangle(a, b, c):
    """
    Tests if the values given could create a right-angled triangle.
    
    :param a: length of one side(expected to be an integer)
    :param b: length of one side(expected to be an integer)
    :param c: length of one side(expected to be an integer)
    
    >> print(is_a_right_triangle(4, 3, 5))
    
    > True
    
    """
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    elif a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2
    else:
        return b ** 2 == a ** 2 + c ** 2
        
