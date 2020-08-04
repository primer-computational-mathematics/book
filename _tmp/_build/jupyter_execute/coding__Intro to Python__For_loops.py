(for_loops)=
# For loops
``` {index} Loops: for loop
```
_For_ loops are used to iterate over elements in a list (or any other iterable structure). Iterating means looping over. The syntax for this type of loop is:

    for element in list:
        # lines of code to be executed
        # more lines of code to be executed
        
The code will loop over all elements in the list and execute the same code for each of them. The code inside _for_ loop needs to be indented. For example:

my_list = [1, 3, 5, 7, 9, 11]
print(my_list)

# For each element in my_list, add 5 and print it

for element in my_list:
    element = element + 5
    print(element)

print(my_list) # The original list does not change

Apart from looping over elements, _for_ loops can be created for specified number of iterations using the _range()_ function. The syntax for _range()_ is:

    range([start], stop, [step])
    
This generates sort of a list with elements between start and stop, excluding stop. If step (increment) is not provided, every number is generated. If you use only one argument, _range(5)_ treats it as a stop value and it starts from 0.

print("range(0, 6, 1)")

for i in range(0, 6, 1):
    print(i)

    
print("\nrange(0, 6, 2)")

for i in range(0, 6, 2):
    print(i)
    
print("\nrange(0, 6)")

for i in range(0, 6):
    print(i)
    
print("\nrange(6)")

for i in range(6):
    print(i)
    

We can generate an index with _range()_ function to loop over elements in a list:

my_list = [1, 3, 5, 7, 9, 11]
print(my_list)

for i in range(len(my_list)): # Range from 0 to length of list
    my_list[i] *= 2 # Modify values in the list
    
print(my_list)    

## Exercise:

Create a _for_ loop to find Celsius temperatures for Fahrenheit temperatures between 20\\(^\circ\\)F and 80\\(^\circ\\)F at 5\\(^\circ\\)F increments. The Fahrenheit-Celsius conversion formula is:

$$ T_{Celsius} = \frac{5}{9}*(T_{Fahrenheit}-32)$$

for temp_F in range(20, 81, 5):
    
    # Calculate the temperature in Celsius
    temp_C = 5./9.*(temp_F - 32)
    
    # Make a nicely formatted print statement
    print("%.2f degrees Fahrenheit is %.2f degrees Celsius." % (temp_F, temp_C))