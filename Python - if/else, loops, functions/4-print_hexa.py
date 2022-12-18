#A program that prints all numbers from 0 to 98 in decimal and in hexadecimal
#using hex() function
for i in range (0, 98):
    print("{0} = {1}".format(i, hex(i)))

"""Other code option;
for i in range(0, 98):
    print(f"{i} = {hex(i)}")
"""
