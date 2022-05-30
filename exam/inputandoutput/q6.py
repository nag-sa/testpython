#Write a program to take three names as input from a user in the single input() function call.

str = input("Enter name:")

lst = str.split(" ")
counter=1
for x in lst:
    print("Name{}: {}".format(counter, x))
    counter = counter+1

