# **kwargs is a special syntax used in the function definition to pass variable-length keyworded arguments.
# It is actually a dictionary of the variable names and its value.
# Here, also, “kwargs” is used just by convention. You can use any other name.

def myattribute(**kwargs):

    for key, value in kwargs.items():
        print(key + " : " + str(value))

myattribute(name = "saurabh", age= 30, city = "Ajmer")
