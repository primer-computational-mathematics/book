#!/usr/bin/env python 

## Maths Methods 1
## Lecture 8 (Modelling)

import numpy
import scipy
import scipy.optimize as optimize
from math import pi, exp

###### NUMERICAL DIFFERENTIATION ######
###### Lecture 8, slide 16 ######
x = numpy.array([0.0, 0.1, 0.2, 0.3, 0.4])
y = numpy.array([0.0, 0.0998, 0.1987, 0.2955, 0.3894])

# The first derivatives are computed using central differences.
# Here, the argument value of 0.1 is the 'sample distance' (i.e. dx)
derivatives = numpy.gradient(y, 0.1)
for i in range(0, len(x)):
   print "The derivative at x = %f is %f\n" % (x[i], derivatives[i])

###### NUMERICAL INTEGRATION ######
###### Lecture 8, slide 32 ######
time = numpy.array([0, 1, 2, 3, 4, 5, 6]) # Time in hours
discharge = numpy.array([0.07, 0.1, 0.06, 0.02, 0.07, 0.06, 0.05]) # Flow rate in m**3/s
time = time*3600.0 # Convert time in hours into time in seconds

integral = numpy.trapz(discharge, x=time) # Integrate using the trapezoidal rule. Units are m**3
print "The integral of the discharge data w.r.t. time is %f\n" % integral


###### FORWARD EULER METHOD ######
###### Lecture 8, slide 70 ######
print "Applying the forward Euler method to solve: dy/dx = 2*x*(1-y)..."
def derivative(x,y):
   return 2*x*(1-y)
n = 7 # Number of desired solution points
dx = 0.4 # Distance between consecutive solution points along the x axis
x = numpy.zeros(n) # x value at each solution point, initially full of zeros.
y = numpy.zeros(n) # y value at each solution point, initially full of zeros.
# Now set up the initial condition. These two lines aren't really needed 
# since we have already initialised each component of the array to zero,
# but we'll put them here for completeness.
x[0] = 0
y[0] = 0 
print "At x = %f, y = %f" % (x[0], y[0]) # Print out the initial condition
for i in range(0, n-1):
   x[i+1] = x[i] + dx
   y[i+1] = y[i] + derivative(x[i],y[i])*dx
   print "At x = %f, y = %f" % (x[i+1], y[i+1]) 


###### ROOT FINDING: BISECTION METHOD ######
###### Lecture 8, slide 83 ######
def f(x):
    return x*exp(x) - 1
# Find the root of the function f(x) using the bisection method.
# We must specify limits a and b in the arguments list
# so the method can find the root somewhere in between them.
root = optimize.bisect(f, a=0, b=1)
# Print out the root. Also print out the value of f at the root, 
# which should be zero if the root has been found accurately.
print "\nThe root of the function f(x) is: %f. At this point, f(x) = %f.\n" % (root, f(root))


###### ROOT FINDING: NEWTON-RAPHSON METHOD ######
###### Lecture 8, slide 114 ######
def f(x):
    return x*exp(x) - 1
# Find the root of the function f(x) using the Newton-Raphson method.
# We must provide the method with a starting point x0 (here we have chosen x0=0).
root = optimize.newton(f, x0=0)
print "The root of the function f(x) is: %f. At this point, f(x) = %f.\n" % (root, f(root))


###### DOMINANT EIGENVALUES ######
###### Lecture 8, slide 156 ######
A = numpy.matrix([[2, 2],
                  [1, 4]])
# For this simple matrix we can use NumPy's eigvals function
# which we have seen before. The max and abs functions have been used
# to pick out the eigenvalue with the largest magnitude.
print "The dominant eigenvalue of A is: %f\n" % max(abs(numpy.linalg.eigvals(A)))

# Note that for sparse matrices, we can use
# the following scipy function. The optional
# argument k is for controlling the desired number of
# eigenvalues returned.
#print scipy.sparse.linalg.eigs(A, k=1)


