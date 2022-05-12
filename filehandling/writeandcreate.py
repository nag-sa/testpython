# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content

file = open("D:\\python\\filehandlingtest.txt","a")
file.write("\nI am in TCS Bangalore")
file.close()
file = open("D:\\python\\filehandlingtest.txt","r")
print(file.read())

#the "w" method will overwrite the entire file.
file = open("D:\\python\\filehandlingtest.txt","w")
file.write("New data, Old data of this file has been overwitten")
file.close()
file = open("D:\\python\\filehandlingtest.txt","r")
print(file.read())

#Create a New File
#To create a new file in Python, use the open() method, with one of the following parameters:
#"x" - Create - will create a file, returns an error if the file exist
#"a" - Append - will create a file if the specified file does not exist
#"w" - Write - will create a file if the specified file does not exist

#Create a file called "myfile.txt":
filenew = open("D:\\python\\myfile.txt", "x") #a new empty file is created!

#Error (File exists) will displayed, if specified file is exists
filenew = open("D:\\python\\myfile.txt", "x")         #error file exists
filenew = open("D:\\python\\myfile.txt", "w")         #error file exists

#Delete a File
#To delete a file, you must import the OS module, and run its os.remove() function:

import os
os.remove("D:\\python\\myfile.txt")

#Delete Folder
#To delete an entire folder, use the os.rmdir() method:
#You can only remove empty folders.

import os
os.rmdir("myfolder")           #give folder name which you want to remove, and it should be empty.