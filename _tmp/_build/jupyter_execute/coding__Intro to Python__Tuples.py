(tuples)=
# Tuples
``` {index} Tuples
```
Tuples are constant lists. They can be used like lists to store data but they cannot be modified (they are immutable). They are used for storing multiple values from functions. They are created like lists, but with round brackets:

    tuple1 = (variable1, variable2, variable3)
   
Tuples can have as many elements as you want and they don't have to be of the same type. Tuples are used, for example, in string formatting syntax:
    
    print("text %g, %g" % (no1, no2)) # (no1, no2) is a tuple
    
For functions that return multiple values, values from tuples can be extracted with this syntax:

    value1, value2 = function1(some_variable)

t = (2, 4, 6, 'temp.pdf')   # Create a tuple.
t =  2, 4, 6, 'temp.pdf'    # Create a tuple, without bracket

print(t[3])                 # Indexing as usual

What is the purpose of tuples, when lists have more functionality?
- Tuples cannot be modified, even by accident.
- They are faster than lists.
- Widely used in Python.
- Can be used as keys in dictionaries, while lists can't.