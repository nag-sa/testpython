#Count the total number of upper case, lower case, and digits used in the text file “merge.txt”.

file = open("D:\\python\\filehandlingtestprog\\merge.txt" , "r")
data = file.read()

countupper = 0
counlower = 0
countdigits = 0

for char in data:
    if char.isupper():
        countupper= countupper+1
    if char.islower():
        counlower= counlower+1
    if char.isdigit():
        countdigits= countdigits+1
print(countupper)
print(counlower)
print(countdigits)

