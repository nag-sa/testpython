#Print words having "h" but not "i" letter in the below sentence: "Hey! How are you? his name is saurabh?"

str = "Hey! How are you? his name is saurabh?"

for word in str.split():

    if "h" in word and "i" not in word:
        print(word)



