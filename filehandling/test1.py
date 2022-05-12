#Create a text file “intro.txt” in python and ask the user to write a single line of text by user input.

file = open("D:\\python\\filehandlingtestprog\\intro.txt" , "w")
userinput = input("Enter user input: ")
file.write(userinput)
file.close()

file = open("D:\\python\\filehandlingtestprog\\intro.txt" ,"r")
print(file.read())