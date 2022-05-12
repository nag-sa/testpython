#print all the groups in dictionary having value with lettre "o" : dict={"group1": "orange", "group2": "red", "group3": "yellow"}

dict={"group1": "orange", "group2": "red", "group3": "yellow"}
for val in dict.values():
    if "o" in val:
        print(val)