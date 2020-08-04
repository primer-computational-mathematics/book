(importing)=
# Importing in Python
``` {index} Importing modules
```
Python's growing popularity over the years has inevitably lead to the development of thousands of excellent libraries and frameworks. This section will cover the basics of importing them, but also cover how to import your own classes, functions and much more.

Often we will want to import many functions and objects from a certain module, so we would simply import the entire module: 

import math

print(math.sin(0))

Importing the whole math module allows us to use everything inside it, such as the sin function. However, if we only need the sin function from the math module, it is good practice to import only that.

from math import sin

print(sin(0))

When imported like this, we no longer need to use the "math." prefix, because this also imported sin into our namespace. If we instead do:

from math import *

print(cos(0))

Here we have imported everything from the math module AND we put everything from it into our namespace. This is generally **not** recommended, as it can overshadow our other functions with the same name. The same can happen if we import a single function. We can avoid this by renaming our imports.

import numpy as np
from math import sqrt as square_root

print(square_root(4))
print(np.ones(5))

If we want to import a function from a specific file, say a file named 'my_module.py' and it is located in the same folder as the python script into which we want to import it, we simply write:

from my_module import my_function

print(my_function(3))

Where my_function is just a square in this case. In general, we can specify a path to our module. For example, if our my_module.py file is on our Desktop, we could import it with:

import os
os.chdir(r'C:\Users\StudentShapers\Desktop')
import my_module