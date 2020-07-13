# _While_ loops
``` {index} Loops: while loops
```
_While_ loops repeat instructions until certain condition is **False** (while the condition is **True**). The syntax is as follows:
    
    while boolean:
        # Some code to be executed while boolean is True
        
    # Some more code to be executed once the while loop is over, executed once
    
Some _while_ loops are infinite, where the condition never becomes **False**. A _while_ loop, similar to _if_ statements, needs the code to be indented.

## Example:

counter = 0 # Set counter

print("Initial counter is: ", counter)

print("\nEntering while loop")

while counter <= 10:
    
    # Add one to the counter until it is equal to 10
    counter = counter + 1
    
    print(counter)
    
print("While loop finished.\n")
    
print("Final counter is: ", counter)

## Exercise:

Create a _while_ loop to find Celsius temperatures for Fahrenheit temperatures between 20$^\circ$F and 80$^\circ$F at 5$^\circ$F increments. The Fahrenheit-Celsius conversion formula is: $$ T_{Celsius} = \frac{5}{9}*(T_{Fahrenheit}-32) $$

temp_F = 20           # Initial temperature in Fahrenheit
dF = 5                # Increment in Fahrenheit

while temp_F <= 80:
    
    temp_C = 5./9.*(temp_F-32) # Calculate the temperature in Celsius
    
    # Make a nicely formatted print statement
    
    print("%.2f degrees Fahrenheit is %.2f degrees Celsius." % (temp_F, temp_C))
    
    # Add increment to the temperature so it increases with each loop
    
    temp_F = temp_F + dF