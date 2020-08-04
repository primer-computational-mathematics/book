(nested_lists)=
# Nested lists
``` {index} Lists: nested lists
```
Lists can contain elements which are also lists.

list1 = list(range(-20, 50, 5))
list2 = list(range(100, 130, 2))

list3 = [list1, list2]

print(list3)       # Print new list
print(list3[0])    # Print list1
print(list3[1])    # Print list2
print(list3[0][1]) # Print second element in first list

Above, we created a table with rows. Using _zip()_ function we can loop through two or more lists at the same time. With that we can create a table with columns:

list4 = []

for i, j in zip(list1, list2):
    row = [i, j]
    list4. append(row)
    
print(list4)

# This can be also done with list comprehension

list5 = [[i, j] for i, j in zip(list1, list2)]
print(list5)