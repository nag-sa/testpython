num = 0
try:
    if num != 2 :
        raise Exception("num is not matching")
except Exception as e:
    print("Exception handled: " + str(e))

finally:
    print("This block will execute, no mattters try or except block will handle error or not")

print("Hello")