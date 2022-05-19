# fibonici series (0,1,1,2,3,5,8,13)

num1 = 0
num2 = 1

print(num1)
print(num2)

i = 0

while i < 5 :
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3
    i = i+1

# finding duplicate charactres in string

str = "saurabhs"
s1 = set()

for char in str:
    if str.count(char) > 1:
        s1.add(char)
print(s1)

# Finding repating charcters count in string "geeksforgeeks"
# o/p = {"g": 2, "e":4, ...}

mystr = "geeksforgeeks"
mydict = {}

for char in mystr:
    charcount = mystr.count(char)
    mydict[char]= charcount  #key is char and value is charcount
print(mydict)

#python count number of digits in integer
# o/p will be 5 (we need to find no. of digit present in integer or here in n)
n = 67892
count = 0
while (n > 0):
    n = n//10  #floor division
    count = count +1
print(count)

#one more way to handle above problem is to , convert int(n = 67892) into string and print length of it.
# n = 67892
# digit = (len(str(n)))
# print(digit)