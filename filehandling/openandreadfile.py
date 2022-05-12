# #open a file and read whole data of file,  using "r"(read) keyword
# # fileopen = open("D:\\python\\filehandlingtest.txt", "r")
# # print(fileopen.read())
#
# #open a file and read whole data of file, without "r"(read) keyword
# fileopen = open("D:\\python\\filehandlingtest.txt")
# print(fileopen.read())
#
# #return/read first 5 chars of the file data
# fileopen = open("D:\\python\\filehandlingtest.txt")
# print(fileopen.read(5))
#
# #return one line by using the readline() method
# fileopen = open("D:\\python\\filehandlingtest.txt")
# print(fileopen.readline())
#
# #By calling readline() two times, you can read the two first lines
# fileopen = open("D:\\python\\filehandlingtest.txt")
# print(fileopen.readline())
# print(fileopen.readline())

#By looping through the lines of the file, you can read the whole file, line by line:
#Loop through the file line by line:

file = open("D:\\python\\filehandlingtest.txt","r")
count = 0
for line in file:
    line = line.replace(".", "")
    if "Ajmer" in line.split():
        print(line)
        count = count + 1
print(count)














