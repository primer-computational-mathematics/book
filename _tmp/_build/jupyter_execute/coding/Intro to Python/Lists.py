# Lists
``` {index} Lists
```
A list is an object that contains multiple elements in defined order (referred to as index number). The syntax is:

    l = [element1, element2, element3, element4, etc..]
    
To extract a specific element or part of the list, we can use slicing syntax:

l = [1, 3, 5, 9, 7, 11]

# Print first element
print(l[0])

# Print elements three to six, returns a list
print(l[2:6])

# Print every other elements but the last two excluded
print(l[0:-3:2])

# Returns class list
print(type(l))

The same operations can be done to lists with strings:

shopping_list = ["potatoes", "cucumber", "apples",
                 "bananas", "milk", "juice"]

# Print first element
print(shopping_list[0])

# Print elements three to six, returns a lis
print(shopping_list[2:6])

# Print every other elements but the last two excluded
print(shopping_list[0:-3:2])

# Returns class list
print(type(shopping_list))

Other operations on lists:

l = [1, 3, 5, 9, 7, 11]

print(len(l))  # Prints the number of elements in the list

l.append(13)   # Appends 13 at the end of the list
print(l)

print(min(l)) # Returns minimum value in the list
print(max(l)) # Returns maximum value in the list

print(sum(l)) # Sums up elements of the list

l = l + [17, 19] # Adds a list [17, 19] at the end of l
print(l)

l.insert(2, 305) # Insert at index 2, number 305
print(l)

del l[2] # Delete the element we inserted at index 2
print(l)

print(l.index(11)) # Return what index value 11 has

print(305 in l) # Check if 305 is in the list