#Write a Program to extract each digit from an integer in the reverse order.
#For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

number = 7536

while number > 0:
    digit = number % 10        #get the last digit
    number = number // 10      #remove the last digit and repeat the loop
    print(digit, end=" ")

