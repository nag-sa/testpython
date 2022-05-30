#Write a program to check if the given file is empty or not

import os

file = os.stat("D:\\repo\\testpython\\exam\\inputandoutput\\test.txt").st_size == 0

print(file)