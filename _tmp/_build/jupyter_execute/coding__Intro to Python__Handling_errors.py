(handling_errors)=
# Handling errors
``` {index} Handling errors
```
When an _error_ occurs in Python, an _exception_ is _raised_. 

(error_types)=
## Error types
The full list of built-in exceptions is available in the [documentation](https://docs.python.org/3/library/exceptions.html#concrete-exceptions).

For example, when we create a tuple with only four elements and want to print the 5th element, we get this error message:

    flower_names = ("iris",
                    "poppy",
                    "dandelion",
                    "rose")

    print(flower_names[4])

    ---------------------------------------------------------------------------
    IndexError                                Traceback (most recent call last)
    <ipython-input-2-3497b57dd596> in <module>
          4                 "rose")
          5 
    ----> 6 print(flower_names[4])

    IndexError: tuple index out of range
    
IndexError refers to incorrect index, such as out of bounds.

(raising_errors)=
## Raising errors
In-built functions trigger or _raise_ errors in Python. We can do that as well by using _raise_:

    raise ValueError

    ---------------------------------------------------------------------------
    ValueError                                Traceback (most recent call last)
    <ipython-input-5-e4c8e09828d5> in <module>
    ----> 1 raise ValueError

    ValueError:
    
## Catching errors
(try_except)=
### Try and except blocks
To handle errors in the code gracefully, we can use _try_ and _except_ blocks to avoid unnecessary crashes of the program. The _try_ block executes the program and if the program fails, exception is raised and we can recover from the error. The syntax is:

    try:
        # some code
    except ExceptionName1:
        # some code
    except ExceptionName2:
        # some code
    …
    except:
        # lines to execute if there was an exception not caught above
    else:
        # lines to execute if there was no exception at all
_else_ is optional, at least one _except_ needs to be raised. An example code below:

a = "ten"

try:
    
    # Try to create a number out of a string
    
    float(a)
    
except ValueError:
    
    # Raise an error if characters are not numbers
    
    print("Exception was raised.\nPlease use digits in your string.")