(flow_control_statements)=
# Flow control statements
``` {index} Break and continue statements
```
(break_continue)=
## Break and continue statements

The _break_ and _continue_ statements are used in loops (_while_ or *for*) to modify behaviour of the loop. _break_ ends the loop, while _continue_ ends the current iteration and continues onto the next one.

Example use of _break_ statement:

counter = 0

while True: # Create an infinite loop
    
    counter += 1
    
    if counter > 29:
        break # Exit the loop if counter is 30 or more
        
print(counter)

Example use of _continue_ statement:

for i in range(10):

    if i%2 == 1: # Skip odd values
        continue
        
    print(i)

(pass)=
## Pass statement
``` {index} Pass statement
```
_pass_ statement is used in the code to "do nothing".

for i in range(10):
    
    if i%2 == 1: # Do nothing for odd numbers
        pass
    else: # Multiply even numbers by 4
        i *= 4
        
    print(i)