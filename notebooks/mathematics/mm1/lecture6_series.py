#!/usr/bin/env python 

## Maths Methods 1
## Lecture 6 (Sequences and series)

import numpy
import pylab
from sympy import sin, cos, exp, ln, Function, Symbol, diff, integrate, limit, oo, series, factorial
from math import pi
#import mpmath

###### SEQUENCES ######
###### Lecture 6, slide 10 ######
# Finite sequence example. The elements of the sequence are stored in a list
finite_sequence = [2*k for k in range(1, 5)] # Remember: range(A,B) generates integers from A up to B-1, so we need to use B=5 here

###### CONVERGENCE OF SEQUENCES ######
###### Lecture 6, slide 11, 13, 14 ######
k = Symbol('k')
print "As k->infinity, the sequence {k} tends to: %f\n" % limit(k, k, oo) # The 'oo' here is SymPy's notation for infinity

print "As k->infinity, the sequence {1/k} tends to: %f\n" % limit(1.0/k, k, oo)

print "As k->infinity, the sequence {exp(1/k)} tends to: %f\n" % limit(exp(1.0/k), k, oo)

print "As k->infinity, the sequence {(k**3 + 2*k - 4)/(k**3 + 1)} tends to: %f\n" % limit((k**3 + 2*k - 4)/(k**3 + 1), k, oo)

###### SERIES ######
###### Lecture 6, slide 15 ######
# Using list comprehension:
print "The sum of 3*k + 1 (from k=0 to k=4) is: %f\n" % sum([3*k + 1 for k in range(0,5)])
# Note: we could also use the nsum function (part of the module mpmath): 
# import mpmath
# print mpmath.nsum(lambda k: 3*k + 1, [0, 4])

x = 1
print "The sum of (x**k)/(k!) from k=0 to k=4, with x = 1, is: %f\n" % sum([x**k/factorial(k) for k in range(1,5)])


###### ARITHMETIC PROGRESSION ######
###### Lecture 6, slide 18 ######
print "The sum of 5 + 4*k up to the 11th term (i.e. up to k=10) is: %f\n" % sum([5 + 4*k for k in range(0,11)])


###### GEOMETRIC PROGRESSION ######
###### Lecture 6, slide 21 ######
print "The sum of 3**k up to the 7th term (i.e. up to k=6) is: %f\n" % sum([3**k for k in range(0,7)])


###### INFINITE SERIES ######
###### Lecture 6, slide 23, 24, 25 ######
# Note: The mpmath Python module is needed to use nsum which can handle sums of infinite series.
# You may need to install it on your computer and uncomment the lines below to use it.
#print "The sum of the infinite series sum(1/(2**k)) is: %f\n" % mpmath.nsum(lambda k: 1/(2**k), [1, mpmath.inf])
#print "The sum of the infinite alternating series sum(((-1)**(k+1))/k) is: %f\n" % mpmath.nsum(lambda k: ((-1)**(k+1))/k, [1, mpmath.inf])


###### RATIO TEST ######
###### Lecture 6, slide 27 ######
# A divergent example
k = Symbol('k')
f = (2**k)/(3*k)
f1 = (2**(k+1))/(3*(k+1))
ratio = f1/f

lim = limit(ratio, k, oo) 
print "As k -> infinity, the ratio tends to: %f" % lim
if(lim < 1.0):
   print "The series converges"
elif(lim > 1.0):
   print "The series diverges"
else:
   print "The series either converges or diverges"

# A converging example
f = (2**k)/(5**k)
f1 = (2**(k+1))/(5**(k+1))
ratio = f1/f

lim = limit(ratio, k, oo) 
print "As k -> infinity, the ratio tends to: %f" % lim
if(lim < 1.0):
   print "The series converges\n"
elif(lim > 1.0):
   print "The series diverges\n"
else:
   print "The series either converges or diverges\n"

   
###### POWER SERIES ######
###### Lecture 6, slide 30 ######
k = Symbol('k')
x = Symbol('x')

a = 1.0/k
f = a*(x**k)

a1 = 1.0/(k+1)
f1 = a1*(x**(k+1))

ratio = abs(a/a1)
R = limit(ratio, k, oo)
print "The radius of convergence (denoted R) is: %f" % R

x = 0.5
if(abs(x) < 1):
   print "The series converges for |x| = %f (< R)\n" % abs(x)
elif(abs(x) > 1):
   print "The series diverges for |x| = %f (> R)\n" % abs(x)
else:
   print "The series either converges or diverges for |x| = %f (== R)\n" % abs(x)
   
###### USEFUL SERIES ######
###### Lecture 6, slide 34 ######
x = Symbol('x')
r = Symbol('r')

# Note: the optional argument 'n' allows us to truncate the series
# after a certain order of x has been reached.
print "\n1/(1+x) = ", series(1.0/(1.0+x), x, n=4)
print "\n1/(1-x) = ", series(1.0/(1.0-x), x, n=4)
print "\nln(1+x) = ", series(ln(1.0+x), x, n=4)
print "\nexp(x) = ", series(exp(x), x, n=4)
print "\ncos(x) = ", series(cos(x), x, n=7)
print "\nsin(x) = ", series(sin(x), x, n=8)


