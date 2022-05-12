#Copy all the groups having value with lettre "o" in a new set called oSet. Copy remaining groups into a list called "notOList".  Print the elements of oSet and notOList. :dict={"group1": "orange", "group2": "red", "group3": "yellow"}

dict={"group1": "orange", "group2": "red", "group3": "yellow"}

oSet = set()
notOList = []

for key, val in dict.items():
    if "o" in val:
        oSet.add(key)
    else:
        notOList.append(key)
print(oSet)
print(notOList)













