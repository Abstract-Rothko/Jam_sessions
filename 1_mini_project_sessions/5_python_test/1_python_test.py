# Python Test
import json
from time import sleep
from datetime import datetime


score = 0
total_score = 30
current_date = datetime.today().date()

sleep(.5)
print("Welcome to the Python Test!")
print("----------" * 6)
name = input("What's your name? ")
sleep(.5)
print(f"Hello, {name}! Answer the following questions as best you can!")
print("----------" * 6)

sleep(1)
print("""
Q1. What is the output of the following code?

    my_list = [1, 2]
    
    for v in range(2):
        my_list.insert(-1, my_list[v])
    print(my_list)

a. [1, 2, 1, 2]
b. [1, 1, 1, 2]
c. [2, 1, 1, 2]
d. [1, 2, 2, 2]
""")
answer_1 = input("> ")

if answer_1 == "b":
    score += 2

sleep(1)
print("""
Q2. The meaning of a positional argument is determined by:
    
a. its position within the argument list
b. the argument's name specified along with its value
c. both
d. there is no correct answer
""")
answer_2 = input("> ")

if answer_2 == "a":
    score += 2

sleep(1)
print("""
Q3. Which of the following statements is true regarding the following code?

    lst = [0, 2, 4, 6, 8]
    other_lst = lst

a. lst and other_lst are different lists
b. lst and other_lst are different names of the same list
c. there is no correct statement
""")
answer_3 = input("> ")

if answer_3 == "b":
    score += 2

sleep(1)
print("""
Q4. An operator that is able to check whether two values are not equal is coded as:

a. =/=
b. !=
c. <>
d. not ==
""")
answer_4 = input("> ")

if answer_4 == "b":
    score += 2

sleep(1)
print("""
Q5. What will the following code output?
    
    1 // 2

a. is equal to 0.5
b. is equal to 0
c. cannot be predicted
d. is equal to 0.0
""")
answer_5 = input("> ")

if answer_5 == "b":
    score += 2

sleep(1)
print("""
Q6. What will the following code output?

    def function(a, b):
        return b ** a
        
    print(function(b = 2, 2))

a. will output None
b. is erroneous
c. will output 4
""")
answer_6 = input("> ")

if answer_6 == "b":
    score += 2

sleep(1)
print("""
Q7. Which of the following variable names is illegal and will cause a SyntaxError:
    
a. in
b. print
c. In
""")
answer_7 = input("> ")

if answer_7 == "a":
    score += 2

sleep(1)
print("""
Q8. What is the correct output to the following code?

    a = 1
    b = 0
    a = a ^ b
    b = a ^ b
    a = a ^ b
    
    print(a, b)

a. 0 0
b. 0 1
c. 1 1
d. 1 0
""")
answer_8 = input("> ")

if answer_8 == "b":
    score += 2

sleep(1)
print("""
Q9. What is the output of the following code if the user enters two lines coding 3 and 6 respectively?

    y = input()
    x = input()
    print(x + y)

a. 3
b. 6
c. 63
d. 36
e. 9
""")
answer_9 = input("> ")

if answer_9 == "c":
    score += 2

sleep(1)
print("""
Q10. What is the output of the following code?

    print('a', 'b', 'c', sep = 'sep')

a. asepbsepc
b. a b c
c. abc
d. asepbsepcsep
""")
answer_10 = input("> ")

if answer_10 == "a":
    score += 2

sleep(1)
print("""
Q11. What is the output of the following code?

    x = 1 // 5 + 1 / 5
    print(x)

a. 0.2
b. 0.4
c. 0.5
d. 0
""")
answer_11 = input("> ")

if answer_11 == "a":
    score += 2

sleep(1)
print("""
Q12. What is the expected output of the following program?

    try:
        print(5/0)
        break
    except:
        print("Sorry, something went wrong.")
    except(ValueError, ZeroDivisionError):
        print("Too bad...")
    
a. the program will cause a SyntaxError exception
b. the program will cause a ValueError exception and output the following message: "Too bad..."
c. the program will cause a ZeroDivisionError exception and output the default error message.
""")
answer_12 = input("> ")

if answer_12 == "a":
    score += 2

sleep(1)
print("""
Q13. Write the following exception in terms of Python.

    6.62607 * 10 ** (-34)
""")
answer_13 = input("> ")

if answer_13 == "6.62607E-34":
    score += 2

sleep(1)
print("""
Q14. You can define your own functions using the def keyword and the following syntax:
    
    def function_name(optional_parameter):
        # the body of the function
        
a. True
b. False
c. SyntaxError
d. def keyword is not required
""")
answer_14 = input("> ")

if answer_14 == "a":
    score += 2

sleep(1)
print("""
Q15. What is term used to describe a function that calls itself.

a. decomposition
b. unpacking
c. recursion
d. indexing
""")
answer_15 = input("> ")

if answer_15 == "c":
    score += 2

sleep(2)
print("Results: ")
print(f"Name: {name}")
print(f"Date: {current_date}")
print(f"Total Score: {score}")

test_percentage = round((score / total_score) * 100, 0)

if test_percentage > 69:
    print(f"You achieved {test_percentage}%. That means you passed!")
else:
    print(f"You achieved {test_percentage}%. To pass the test you need 70%")
    
sleep(2)
chart = input("Can we record your stats (yes/no)? ")
if chart.lower() == "yes":
    file = open('records.json', 'a')
    data = {
        'name': name,
        'total_score': score,
        'pass_percentage': test_percentage
    }
    json.dump(data, file)
    file.write('\n')
    file.close()
    print("Thank you.")
else:
    print("No worries! Next Time!")