(sets)=
# Sets
``` {index} Sets
```
Sets are a type of Python container that are equivalent to sets in maths. They can only contain one copy of a particular element and they are not ordered. They don't have indices or keys. Elements in a set can be of any type.

Sets are defined with curly brackets:

    set1 = {variable1, variable2, variable3, etc...}
Sets only contain one copy of the same element, so even though we specify it twice, a set stores it once:

set1 = {1, 4, 5, 2, 3, 1}
print(set1)

We can see that the values are returned in no particular order.

Sets cannot be added together with simple addition method like lists can. They cannot be sliced or indexed. Operations that can be done on a set:

set2 = {"potato", "banana", "carrot", 4, 5}

set3 = set2 - set1 # Remove elements from set2 that are in set1
print(set3)

print(4 in set2)  # Check if 4 is in set2

print(set2.add("cucumber")) # Add an element to set
print(set2)

set4 = set() # Create an empty set
print(set4)