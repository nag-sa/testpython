"""
SET

1. A set is a collection which is unordered, unchangeable*, and unindexed.
2. Sets are unordered, so you cannot be sure in which order the items will appear.
3. Sets cannot have two items with the same value,  not allowed duplicate values.
4. Set items are unchangeable, but you can remove items and add new items.
5. Sets are written with curly brackets.

"""
set1 = {"a", "b", "c", "a", 1,2,3,}
print(set1)

print(type(set1))

#Add an item to a set, using the add() method
set1.add("z")
print(set1)

#To add items from another set into the current set, use the update() method.
set1 = {"a", "b", "c", "a", 1,2,3,}
set2= {"x", "y", "z", 4,5,6}
set1.update(set2)
print(set1)

#To remove an item in a set, use the remove(), or the discard() method.
s1 = {"abc","xyz", "lmn"}
s1.remove("xyz") # error raised when element doesn't exist.
s1.discard("eshita") # no error raised, when element doesn't exist
print(s1)

#last element remove using pop method
s1.pop()
print(s1)

#to clear set
#s1.clear()
#print(s1)#it will return empty set

#The union() method returns a new set with all items from both sets:
s3 = set1.union(set2)
print(s3)

#Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
