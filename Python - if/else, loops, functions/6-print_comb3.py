#A program that prints all possible different combinations of two digits.
"""
Numbers must be separated by ,, followed by a space
The two digits must be different
01 and 10 are considered the same combination of the two digits 0 and 1
Print only the smallest combination of two digits
Numbers should be printed in ascending order, with two digits
"""
for digit1 in range(0, 10):
    for digit2 in range(digit1 + 1, 10):
        
        print("{}{}".format(digit1, digit2), end=", ")