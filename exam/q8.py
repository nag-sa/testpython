#Given two integer numbers return their product only if the product is greater than 1000, else return their sum.

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

num3 = num1 * num2

if num3 > 1000:
    print(num3)
else:
    print(num1 + num2)




