(functions)=
# Creating custom functions
``` {index} Creating functions
```
Functions in Python are blocks of code that will only be executed when called. They look like this:

    def function_name(arg1, arg2, ...):
        # some code to execute
        return # return some variables, optional

Function names should be descriptive. The arguments are separated by commas and will become local variables within the function. Any object, and any number of objects, can be returned from a function.

Functions have to appear in the code before you execute them:

a = 1
b = 2

# Create a function

def subtract_numbers(a, b):
    return "%g - %g = %g" % (a, b, a-b)

# Call created function

print(subtract_numbers(a, b))
print(subtract_numbers(17,5))
print(subtract_numbers(9, 28))

Even though we have variables a and b in the code, the function does not use them unless they are arguments to the function. Variables 'a' and 'b' inside the function are local variables and they only exist there. If we want to use global variables (variables outside of the function), the code will look like this:

a = 10

# Create a function

def add_to_variable_a(b):
    global a  # Make 'a' a global variable
    a += b
    return a

# Call the function

print("a =", add_to_variable_a(2))
print("a =", add_to_variable_a(4))

# Note how variable a changed