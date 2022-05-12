## Q1: Print even chars in a string ("saurabh")

str = input("Enter a string: ")

for index, char in (enumerate(str)):
    if index % 2 == 0:
        print(index, char)




