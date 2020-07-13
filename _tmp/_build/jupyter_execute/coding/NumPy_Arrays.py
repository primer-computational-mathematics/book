# NumPy Arrays

Numerical Python (NumPy) provides excellent support for working with large arrays in python, along with an extensive library of mathematical functions to operate on these arrays. This notebook will introduce data types in NumPy, how to initialise an array of complex numbers, generating random arrays and array manipulation basics.

## Creating and manipulating arrays

It is important to correctly initialize the array, which includes assigning it a data type. The full list of supported data types in NumPy can be found [here](https://numpy.org/devdocs/user/basics.types.html). It is generally a good idea to work in double precision (float64 data type), unless we are confident in what we are doing.

Each numpy array has an attribute dtype which lets you check its data type. Let us initialise a 2D array of integer numbers and demonstrate this.

import numpy as np

A = np.array([[3, 3, 2],
              [4, 4, 1],
              [0, 6, 2],
              [0, 8, 1]])

print(A.dtype)

To avoid this, we could have simply added a dot after an integer, which python then recognises as a floating point number (float64). NumPy offers several ways of assigning data types. Here are some of the more common ones:

a = 1   # integer
b = 1.  # dot makes it a float
print(type(a), type(b))

A = np.arange(10)  # integers
print(A)
print(A.dtype)

A = np.arange(10, dtype=np.float64)  # assign dtype
print(A)
print(A.dtype)

A = np.arange(10).astype(type(b))  # make array same dtype as b
print(A)
print(A.dtype)

NumPy also allows us to create (pseudo) **random** arrays using numpy.random. Let us initialise a random array of **complex** numbers, which have a real and imaginary component (in python, and often in engineering, the imaginary unit is $j$). We will also seed the generator using np.random.seed(), so that every time we run the code we will get the same 'random' numbers.

np.random.seed(0)  # it does not matter what the seed is (here 0)
B = np.random.rand(3, 3) + 1j * np.random.rand(3, 3)

print(B)
print(B.dtype)

NumPy arrays are more difficult to manipulate than lists, where, for example, lists allow appending and arrays do not. There are, however, numpy functions which allow us to do this in a slightly more tedious way, but with much more control over it.

For example, numpy.**concatenate** joins two or more arrays along an existing axis.

a = np.array([[1, 2], 
              [3, 4]])
b = np.array([[5, 6]])

c = np.concatenate((a, b), axis=0)
print('axis=0: \n', c)

c = np.concatenate((a, b.T), axis=1)
print('axis=1: \n', c)

In the first example, the two arrays were joined along axis=0, i.e. a row was appended. In the second example we wanted to join them along axis=1, which is a column. NumPy arrays require that the lengths of rows and columns match in every column or row vector, so we had to **transpose** the vector b using b.T.

What if we wanted to make a 3D array out of two 2D arrays? This is what NumPy calls **stacking** and has a general function numpy.stack() to achieve this, where we now specify a new axis along which we want to stack our arrays. Let us stack two 2D arrays along a vertical (depth) axis, axis=2.

a = np.array([[1, 2], 
              [3, 4]])
b = np.array([[5, 6],
              [7, 8]])

c = np.stack((a, b), axis=2)
print(c)
print('c.shape: ', c.shape)

Some NumPy functions allow us to specify array shape while creating them. We can also **reshape** any array after they are created.

A = np.zeros((3,3))  # 3x3 array filled with 0s

print(A)

a = np.arange(8)   # 1D array of 8 elements
print(a)

b = a.reshape((4,2))  # reshape to a 4x2 matrix
print('reshape((4,2)): \n', b)

c = a.reshape((2,2,2))  # reshape to a 2x2x2
print('reshape((2,2,2)): \n', c)

As stated before, numpy arrays require a consistent length of rows and columns. In the above example we initialised a 1D array of 8 elements, so the only possible shapes (after reshaping) are 8x1, 4x2, 2x4, 1x8 for 2D and 8x1x1, 4x2x1, 2x2x2, and so on for 3D. 

## Indexing and slicing

NumPy arrays allow for some advanced indexing options, such as **negative indexing** and **boolean indexing**. 

A = np.arange(16).reshape((4, 4))
print(A)

print('A[-1, 2] = ', A[-1, 2])  # last row, third column

print('A < 6 :', A[A < 6])
print('A > 5 and A < 10 :', A[np.logical_and(A > 5, A < 10)])

If we are interested in finding the index of values equal to or less/greater than something, we could use **np.argwhere()**.

print('A == 0: \n', np.argwhere(A == 0))
print('A > 13: \n', np.argwhere(A > 13))

Slicing arrays follows the usual format of A[start:stop:step], where we can specify the starting and stopping index and step size for each dimension, separated by a comma. If a starting index is not specified it is set to 0 by default. If the stop index is not specified, it is the last index (-1) by default. Default step size is 1. Analogue to negative indexing, we can also define slicing with negative start, stop and step sizes, which will then go from the end of the array.

a = np.linspace(10, 100, 10)
print('a =', a)

print('a[3:10] =', a[3:10])  # default step=1
print('a[:6:2] =', a[:6:2])  # up to 6th element, every 2nd element
print('a[::-1] =', a[::-1])  # all elements, but backwards

# start from the last element, go backwards up to 5th from last
print('a[-1:-5:-1] =', a[-1:-5:-1])

A = np.arange(16).reshape((4, 4))
print('\n A = \n', A)

print('A[:, 3] = ', A[:, 3])  # all row elements, only 3rd column

# take all rows, reverse columns
print('\nA[:, ::-1] = \n', A[:,::-1])