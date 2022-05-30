#Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.

def exponent(base, exp):
    result = 1
    for i in range(1,exp+1):
        result = result * base

    print(base, "raises to the power of", exp, "is: ", result)

exponent(2, 3)
