def my_attribute(a, b, c):
    print(a + " "+ b + " "+ c)
    print("This is my attribute")

def my_calling():
    my_attribute("nag", "saurabh", "mathur")
    print("calling other function")
my_calling()


def twonosum(a, b):
    c = a+b
    assert (c == 5)
    print("assertion is pass")
twonosum(3,2)
