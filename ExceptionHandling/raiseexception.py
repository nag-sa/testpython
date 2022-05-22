num = 0
try:
    if num != 2 :
        raise Exception("num is not matching")
except Exception as e:
    print("Not handling Exception: " + str(e))
    raise e

print("Hello")

