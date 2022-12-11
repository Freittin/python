# print 3 times a string stored in the variable str, followed by its first 9 characters.
str = "Holberton School"
print(f"{str*3}, \n")
print(f"{str[:9]}")

word = "Holberton"
# YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE
print(f"First 3 letters: {word[:3]}")
print(f"Last 2 letters: {word[-2:]}")
print(f"Middle word: {word[1:-1]}")

#print object-oriented programming with Python
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[39:66] + str[106:112] + str[:6]
print(str)

#primting the zen of python by Tim Peters
import this