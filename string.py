# Looping thru characters
name = "eshita"
for x in name:
    print(x)

# Length of string
print("the length of the name is", len(name))

# in/not in to check if char present in string
str = "Saurabh"
if "e" in str:
    print("e is present");
else:
    print("e is not present")

# print 4th charcter fron str
print(str[3])

# Check string in a para
para = "hello everyone, how are you doing"
if "buddy" in para:
    print("true")
else:
    print("false")
print("buddy" not in para)

# sub string saurabh from 2nd to 3rd charter using +ve index
print(str[1:3])
print(str[-6:-4])
print(str[:3])  # Sau
print(str[3:])  # rabh
print(str.upper())
print(str.lower())
print(para.split())
para1 = "hi there! how are you"
print(para1.split('!'))

name1 = "Saurabh "
name2 = "Nag"
name3 = print(name1 + " "+ name2)

txt = "my name is {}. i am from {}. my age is {}"
print(txt.format("\"saurabh\"" , "rajasthan", 30))
print(txt.format("eshita" , "bhopal", 30))

list = []; #falsy --> empty list, tuple, dict, set and 0
if not list:
    print("List is empyty")

