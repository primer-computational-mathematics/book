# _If_ construct
``` {index} If statement
```

_If_ construct allows to create cases in the code based on conditions:

    if boolean:
        # Executue some code if boolean is True
    elif boolean2:
        # Execute some code only if boolean is False and boolean2 is True
    else:
        # Execute some code only if boolean is False and boolean2 is False
        
_elif_ and _else_ are optional blocks. Code inside each block needs to be indented.

## Example use:

number = 10

if number < 5:
    print("%g is less than 5." % (number))
elif number < 12:
    print("%g is less than 12." % (number))
else:
    print("%g is greater or equal to 12." % (number))
    
# If statements in one line
a = 1 if number == 5 else 0
print(a)