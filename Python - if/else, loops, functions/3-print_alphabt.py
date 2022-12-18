#program that prints the ASCII alphabet, in lowercase, not followed by a new line.
#Print all the letters except q and e
for i in range(97, 123):
    if i != (101, 113):
        print("{:c}" .format(i), end= '')