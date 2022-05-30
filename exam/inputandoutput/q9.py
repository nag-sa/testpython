#Read line number 4 from the following file

file = open("D:\\repo\\testpython\\exam\\inputandoutput\\test.txt", "r")
linenumber =1

for line in file:
    if linenumber == 4 :
        print(line)
    linenumber = linenumber + 1

