name= "Frank"
age= 44
#How to Use %-formatting
print("Hello, %s."%name)
#arranging ideas via the str.format() method
print("Hello, {}. You are {}.".format(name, age))
#print the values in between
for i in range(2, 10, 2):
    print(i, end=" ")

#prove c is fun
a = 12
if a < 2:
    print("Holberton")
elif a % 2 == 0:
    print("C is fun\n")
else:
    print("School")
print("Programming is like building a multilingual puzzle\n")

b = { 'id': 89, 'name': "John", 'projects': [1, 2, 3, 4] }
b.get('projects')[3]