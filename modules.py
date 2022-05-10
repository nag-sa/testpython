Python Modules:
# A file containing a set of functions you want to include in your application.
#To create a module just save the code you want in a file with the file extension .py
#we can use the module we just created, by using the import statement

Variables in Module
#The module can contain functions, as already described, but also variables of all types (arrays, dictionaries, objects etc):

Naming a Module
#You can name the module file whatever you like, but it must have the file extension .py

Re-naming a Module
#You can create an alias when you import a module, by using the "as" keyword.Ex:
#import mymodule as mmod   #mmod is a alias of mymodule 

Built-in Modules
#There are several built-in modules in Python, which you can import whenever you like. Ex:
# import random , import platform ,  import input , import date

Using the dir() Function
#There is a built-in function to list all the function names (or variable names) in a module. The dir() function. 
#The dir() function can be used on all modules, also the ones you create yourself.
Ex: 
 import platform
x = dir(platform)   #List all the defined names belonging to the platform module
print(x)

Import From Module
#You can choose to import only parts from a module, by using the "from" keyword.
from mymodule import person1     #here we are only importing only person1 details from mymodule file using keyword from






