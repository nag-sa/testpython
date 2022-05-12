#Write a program to read the contents of both the files created in the above programs and merge the contents into “merge.txt”. Avoid using the close() function to close the files.
file = open("D:\\python\\filehandlingtestprog\\intro.txt", "r")
data = file.read()
print(data)
file1 = open("D:\\python\\filehandlingtestprog\\MyFile.txt", "r")
data1 = file1.read()
print(data1)

mergefile = open("D:\\python\\filehandlingtestprog\\merge.txt", "a")
mergefile.write(data +"\n")
mergefile.write(data1)



