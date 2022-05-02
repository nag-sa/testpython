x = 5  # it is assumed as int
y = "hello"  # it is assumed as str

# varibales changes their data type based on assigned values
x = "saurabh"
x = 7

# Type casting
a = str(3)  # output will be "3"
b = int(3.6)  # output will be 3
c = float(3)  # output will be 3.0
print(a)
print(b)
print(c)
print(type(a))
print(type(b))
print(type(c))

# Single line assigment of multiple varibales
d, e, f = 5, "orange", 8.90
print(d)
print(e)
print(f)

# signle vale to multiple variables
name1 = name2 = name3 = "hello dear"
print(name1 , name2 , name3)

fruits = ["apple", "orange","kela"]
p , q , r = fruits
print(p)
print(q)
print(r)

# Print with multiple varibales batter to use comma (,) as (+) doesn't support varibales with different data types.
x1 = 5
x2 = "hello"
print(x1 , x2 ) # will give 5 hello as output
#print(x1 + x2)   # will give error


# global varibale

#Z1 = "hello function"
def add():
    a1 = "varibale inside function"
    print(a1);
add();





