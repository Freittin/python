#A program that prints numbers from 0 to 99
"""
Numbers must be separated by [,], followed by a space
Numbers should be printed in ascending order, with two digits
The last number should be followed by a new line
"""
for i in range(0, 100):
    
    print(f"{i:02d}", end=", ")

#other code print("{:02d}".format(i), end=", ")