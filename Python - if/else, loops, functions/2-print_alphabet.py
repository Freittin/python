# program that prints the ASCII alphabet, in lowercase, not followed by a new line.
for i in range(97, 123):
    print("{:c}".format(i), end='')
print(" ")
#the code ends here

#how to print binary code in python or we use bin() function
print("{0:b}".format(101))

print(bin(22))