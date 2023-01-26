"""Sets"""

#Set
myset = {"apple", "banana", "cherry"}

#Duplicates Not Allowed
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

#Get the Length of a Set
thisset = {"apple", "banana", "cherry"}

print(len(thisset))

#Set Items - Data Types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


set1 = {"abc", 34, True, 40, "male"}

#type()
myset = {"apple", "banana", "cherry"}
print(type(myset))

#The set() Constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


"""Access Set Items"""
#Access Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)



"""Add Set Items"""

#Add Items
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

#Add Sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)


#Add Any Iterable
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)


'''Remove Set Items'''

#Remove Item
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)


thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)



thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)


thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)




'''Loop Sets'''

#Loop Items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)


'''Join Sets'''

#Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)


#Keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)

print(x)


#Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)

print(x)