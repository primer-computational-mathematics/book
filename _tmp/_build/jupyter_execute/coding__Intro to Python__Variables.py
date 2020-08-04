(variables)=
# Variables
``` {index} Variables
```

A variable is an object that contains an assigned value:

a = 10         # a is a variable containing a number
b = "hello"    # b is a variable containing a string (text)

Certain words have a special meaning in Python and cannot be used as variable names. These are: *and, as, assert, break, class, continue, def, del, elif, else, except, exec, finally, for, from, global, if, import, in, is, lambda, not, or, pass, print, raise, return, try, with, while,* and *yield*.

Good variable names are usually descriptive, can be one letter symbols, abbreviation of words, containing lower/upper case, underscores, digits. They cannot start with digits. Variables are case sensitive so variable "a" is not the same as "A".

(variable_types)=
## Types of variables
Common types of Python variables are:
- _str_ - string, e.g. "Hello world!"
- _int_ - integer numbers, e.g. 5
- _float_ - floating point numbers, e.g. 5.0, 5.2
- _bool_ - boolean value, i.e. True or False

Integer and floating point numbers are different variables because of how a computer stores them. Computers use a discrete representation of numbers, which means that there is a gap between two adjacent numbers. For integers this gap is 1 and for floats it is much much smaller. For example, in integer arithmetic 0 and 0.999999 are the same numbers. We will therefore almost always use floating point numbers.

a = int(0.99999999)
b = int(1.00000001)
print(a, b)

To check what type a variable is, we can use the in-built _type()_ function that takes the variable as an argument:

a = "some text"     # A string
b = 5               # An integer
c = 5.              # A float
d = True            # A boolean value

print(type(a))
print(type(b)) 
print(type(c))
print(type(d))

(variable_operations)=
## Operations on variables
### Numbers
An integer-type variable will automatically change to float if it is required for mathematical accuracy:

b = 10      # An integer
b = 1 + b   # b should be still an int
print(b, type(b))

b = 1.1 + b # b should change into float
print(b, type(b))

b = 10      # An integer
b = b/4     # A float
print(b, type(b))

We can make calculations on numbers stored in variables and program mathematical formulae. For example, a position for a ball in vertical motion is given by:
     \\(y(t) = v_0t- \frac{1}{2}gt^2 \\)
where the ball starts at $y=0$ at time $t=0$ and:

* $y$ is the height (position) as a function of time $t$
* $v_0$ is the initial velocity (at $t=0$)
* $g$ is the acceleration due to gravity

Given $v_0$, $g$ and $t$, we can compute the value $y$:

v0 = 12.5  # m/s
g = 9.81   # m/s2
t = 0.3    # s
y = v0*t - 0.5*g*t**2
print("The position of the ball at time t = %.2f s, is y = %.2f m." % (t, y))

### Strings
We can add strings together:

a = "some text"            # A string
print(a, type(a))
a = a + " and more text"   # Add a string at the end of 'a'
print(a, type(a))

You can slice strings to get specific parts of them by using the following syntax:

# Print characters 0, 1 excluding 2
# (Python counts from zero!!!)
print(a[0:2])

# Print all characters but last two
print(a[0:-2])

# Print every second character
# from first 10 characters
print(a[0:10:2])

Searching strings:

s = "To what use serves learning, if understanding be away."

print(s)
print(s.find("use"))  # returns the index of the first character if found
print("if" in s)      # returns True if string 'if' is contained in 's', False otherwise
print("is" not in s)  # returns True if string 'is' is not contained in 's', False otherwise

s2 = s.replace("learning", "studying")  # replaces learning with studying in 's'
print(s2)

s3 = s.replace("learnning", "studying")  # does nothing if we make a typo
print(s3)

Splitting and joining:

s = "Dare to be wise; begin!"
words = s.split()       # Splits the string based on spaces
print(words)

phrases = s.split(";") # Add a string by which splitting will happen
print(phrases)

print(":".join(phrases)) # Join phrases with a collon

Other useful functions:

s = "I like watermelons! I like trains! I like books!"

print(s.count("!"))      # Count how many times string '!' occurs in 's'
print(s[5].isnumeric())  # Check if the sixth character is a number
print(s.lower())         # Make all characters lower case
print(s.upper())         # Make all characters upper case
print(s.isalpha())       # Check if all characters are letters
print(s[2:5].isalpha())  # Check if the characters 3 to 5 are letters

s = "    " + s + "    "
print(s)
print(s.strip())         # Strips strings from tabs, spaces, new line characters from
                         # beginning and end of the string
    
print(len(s))            # Print how many characters the string has

### Booleans

Booleans are objects in Python that are **True** or **False**. The simplest booleans are:

print(True)
print(False)

Objects can be compared to one another, where print statements will return True or False. Standard mathematical formulae in Boolean expressions are:
- $a = b$ is a == b
- $a \neq b$ is a != b
- $a > b$ is a > b
- $a \geq b$ is a >= b
- $a < b$ is a < b
- $a \leq b$ is a <= b 

An example use below:

a = 5
print(a > 10)
print(a == 10)
print(a <= 5)
print(a != 5)
print(a != "cat")

Compound conditions with logical operators can also be used:

a = 5
b = 20

print((a < 6) and (b > 18)) # For 'and' both expressions need to be True to return True
print((a < 5) and (b > 18)) # Returns false because the first expression is False
print((a < 5) or (b > 18))  # For 'or' only one expression is needed to be True

# 'and' and 'or' can be combined, but brackets matter!!

print((a > 10 and b < 10) or b > 13)
print(a > 10 and (b < 10 or b > 13))