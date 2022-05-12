#copy all odd no. b/w 0-20(except 11, 3) in a list called, oddlist and print the odd list.

oddlist = []

for x in range (1, 21, 2):
    if x != 11 and x != 3:
        oddlist.append(x)
print(oddlist)


