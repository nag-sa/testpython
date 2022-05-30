# *args is a special syntax used in the function definition to pass variable-length arguments.
# “*” means variable length and “args” is the name used by convention. You can use any other.

def addtion(a,b,*args):
    print(a,b,*args)
    mul = a*b
    for num in args:
        mul = num * mul
    print(mul)

addtion(1,2,3,4,5)