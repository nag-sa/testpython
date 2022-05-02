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
