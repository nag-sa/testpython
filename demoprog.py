## Q: Print even chars in a string
str = "eshita"
x=0;
for letter in str:
    if x % 2 ==0:
        print(letter)
    x = x+1


## Q: Print words having "h" but not "l" letter in the below sentence
para = "hello saurabh how are you"
for word in para.split():
    if "h" in word and "l" not in word:
        print(word)
        
 #print all the groups having value with lettre "o"
dict={"group1": "orange", "group2": "red", "group3": "yellow"}
for key , value in dict.items():
    #print(key, value)
    if "o" in value:
        print(key)
