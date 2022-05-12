#Create a text file “MyFile.txt” in python and ask the user to write separate 3 lines with three input statements from the user.

file1 = open("D:\\python\\filehandlingtestprog\\MyFile.txt" , "w")
userinput1 = input("Enter first user input: ")
userinput2 = input("Enter second user input: ")
userinput3 = input("Enter third user input: ")

file1.write(userinput1 + "\n" + userinput2 + "\n" + userinput3)

file1.close()

file1 = open("D:\\python\\filehandlingtestprog\\MyFile.txt" , "r")
print(file1.read())

