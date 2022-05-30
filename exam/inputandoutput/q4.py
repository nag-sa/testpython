#Accept a list of 5 float numbers as an input from the user

lst = []
str = input("Enter user number:")

for x in str.split(", "):

    lst.append(float(x))

print(lst)
