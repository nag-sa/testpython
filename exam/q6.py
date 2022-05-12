#Write a program to find whether a string is pallindrome or not. The output should be true/false.
#kanak
#str = input("Enter string: ")

str = "hello"
print(str)

str1 = str[::-1]
print(str1)

if str == str1:
    print("pallindrom")
else:
    print("not pallindrom")




