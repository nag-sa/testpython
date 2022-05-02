"""
LIST

1. list elements can be accessed by index starting from 0
2. List is ordered, order will not change
3. List is mutable (allow changes), we can manipulate list after it has been created
4. List allow duplicates, we can insert same element multiple times in list
5. list can contain element of different data types

Tuple
1. Tuple is immutable (not allow changes), we cann't manipulate tuple after it has been created
2. other features are similar like list 
"""

#List Construction
lst = ["saurabh" , "eshita"]
lst = list(("saurbh", "eshita"))
print(lst)

#List indexing
print(lst[1])
print(lst[-1])

#get sublist
l2 = ['a', 'b', 'c', 1, 2, 3]
print(l2[1:4]) #prints list o/p will be b,c,1

#membefship check
print(4 in l2)

#list length
print(len(lst))

#Add elements
lst.append("apple")
print(lst)

#change list element at particular index
l2[1] = 'd'
print(l2)

#insert operation --> will insert element without replacement of existing element
l2.insert(1, "b")
print(l2)

l3 = (l2 + lst)
print(l3)
print(l2)

#extend any existing list to include another list
l2.extend(lst)
print(l2)

#to remove any item from list
l2.remove("a")
print(l2)

#remove element from any index
l2.pop(4)
print(l2)

#remove all elements from the list
l2.clear()
print(l2)

l2 = ['a',1,2, 4, 3, 5, 6,7 , "hello"]
#loop using membership operator
for x in l2:
    print(x)

#loop using for and range
print("This is range {}".format(range(len(l2))))
for index in range(len(l2)):
    print(l2[index])

#loop using while or while loop
y = 0
while y < len(l2):
    print(l2[y])
    y = y+2

#list sort
lst3 = [2, 1, 10, 6, 5, 11, 3,]
#revese
lst3.reverse()
print(lst3)
#sort
lst3.sort()
print(lst3)
#list sort decending
lst3.sort(reverse= True)
print(lst3)
#list sort case insensitive
#lst3.sort(key= str.lower())
#print(lst3)





