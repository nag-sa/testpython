def numCheck():
    num=0;
    if(num !=1):
        raise Exception("number is not 1")
try:
    numCheck()
except Exception as e:
    print("Handled")

print("Finalyy this got printed")