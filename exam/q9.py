#Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

num = 11
prev = 0
txt = "Prev num: {}, Current num: {}, Sum: {}"
for current in range(num):
    print(txt.format(prev, current, prev+current))
    prev=current
