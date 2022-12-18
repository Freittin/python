"""
program will assign a random signed number to the variable number
"""
import random
number = random.randint(-10, 10)
if number > 0:
    print(f"{number:d} is positive")
    #print("{} is positive".format(number))
elif number == 0:
    print(f"{number:d} is zero")
elif number < 0:
    print("{} is negative".format(number))