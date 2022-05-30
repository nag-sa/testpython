#Write all content of a given file into a new file by skipping line number 5

file = open("D:\\repo\\testpython\\exam\\inputandoutput\\test.txt", "r")

linenumber = 1

for line in file:
    if linenumber != 5 :
        print(line)
    linenumber = linenumber+1

