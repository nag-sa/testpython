#Dictionaries are used to store data values in key:value pairs.
#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#define dictionary
dict = {"name": "saurabh", "age": 30, "gender":"male", "age": 35, "colors":["red", "green", "blue", "blcak"],"year": 1988}

#Print dictionary
print(dict)

# find out type of dictionary
print(type(dict))

#length of dictionary
print(len(dict))

#get the value of any key
x = dict.get("gender")
print(x)

#print list of keys of dict 
y= dict.keys()
print(y)

#print list of values 
z = dict.values()
print(z)

#Adding new key along with value in dict
dict["car"]= "zen"
print(dict)   #or adding new value using update command 
dict.update({"car":"zen"})
# print(dict)

#changing existing key value in dict
dict["name"]="nag"
print(dict)    #or changing existing key value using update command 
dict.update({"name":"nag"})
#print(dict)
#print dict and result will be in form of tuples 
z= dict.items()
print(z)

#The pop() method removes the item with the specified key name
dict.pop("gender")
print(dict)

#Print all key names in the dictionary using for loop
for i in dict:
	print(i)
	
#Print all values in the dictionary using for loop
for i in dict:
	print(dict[i])
	
#print all values using value() method via for loop
for i in dict.values():
	print(i)
	
#print all keys using keys() method via for loop
for i in dict.keys():
	print(i)
	
#Loop through both keys and values, by using the items() method
for i,j in dict.items():
	print(i ,j)
	
#Copy a Dictionary
#Make a copy of a dictionary with the copy() method:
newdict = dict.copy()
print(newdict)

#Make a copy of a dictionary with the dict() function:
#dictnew = dict(dict)
#print(dictnew)

# Interchange/ swapping b/w key and value using for loop
old_dict= {'a':10,  'b': 20, 'c':30}
new_dict= {}

for key,value in old_dict.items():
	print(key , value)
	new_dict[value]=key
print(new_dict)
