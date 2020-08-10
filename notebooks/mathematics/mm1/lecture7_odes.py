#!/usr/bin/env python 

## Maths Methods 1
## Lecture 7 (ODEs)

import numpy
import pylab
from math import pi, exp
from sympy import sin, cos, Function, Symbol, diff, integrate, dsolve, checkodesol, solve, ode_order, classify_ode, pprint

###### ORDER OF AN ODE ######
###### Lecture 7, slide 9 ######
t = Symbol('t') # Independent variable
eta = Symbol('eta') # Constant
v = Function('v') # Dependent variable v(t)
ode = diff(v(t),t) + eta*v(t) # The ODE we wish to solve. Make sure the RHS is equal to zero.
print "ODE #1: \n"
pprint(ode)
print "The order of ODE #1 is %d\n" % ode_order(ode, v(t))

x = Function('x') # Dependent variable x(t)
m = Symbol('m') # Constant
k = Symbol('k') # Constant
ode = m*diff(x(t),t,2) + k*x(t)
print "ODE #2: \n"
pprint(ode)
print "The order of ODE #2 is %d\n" % ode_order(ode, x(t))

y = Function('y') # Dependent variable y(t)
ode = diff(y(t),t,4) - diff(y(t),t,2)
print "ODE #3: \n"
pprint(ode)
print "The order of ODE #3 is %d\n" % ode_order(ode, y(t))


###### ANALYTICAL SOLUTIONS ######
###### Lecture 7, slide 14 ######
x = Symbol('x') # Independent variable
y = Function('y') # Dependent variable y(x)

# The ODE we wish to solve. Make sure the RHS is equal to zero.
ode = diff(y(x),x) - 2*x*(1-y(x))
solution = dsolve(ode, y(x)) # Solve the ode for function y(x).
print "ODE #4: \n"
pprint(ode)
print "The solution to ODE #4 is: ", solution

# This function checks that the result of dsolve is indeed a solution
# to the ode. Basically it substitutes in 'solution' into 'ode' and
# checks that the RHS is zero. If it is, the function returns 'True'.
print "\nChecking solution using checkodesol..."
check = checkodesol(ode, y(x), solution)
if(check[0] == True):
   print "y(x) is indeed a solution to ODE #4.\n"
else:
   print "y(x) is NOT a solution to ODE #4.\n"
   
# The mpmath module can handle initial conditions (x0, y0) when solving an
# initial value problem, using the odefun function. However, this will
# not give you an analytical solution to the ODE, only a numerical
# solution. The print statement below compares the numerical solution
# with the values of the (already known) analytical solution between x=0 and x=10.
# Remember to uncomment the lines below if you have the mpmath module installed.
#import mpmath
#f = mpmath.odefun(lambda x, y: 2*x*(1-y), x0=0, y0=2)
#for x in numpy.linspace(0, 10, 100):
   #print(f(x), 1.0 + exp(-x**2))

###### SEPARATION OF VARIABLES ######
###### Lecture 7, slide 20 ######
x = Symbol('x') # Independent variable
y = Function('y') # Dependent variable y(x)
# The ODE we wish to solve.
ode = (1.0/y(x))*diff(y(x),x) - cos(x)
print "\nODE #5:"
pprint(ode)
# Solve the ode for function y(x).using separation of variables.
# Note that the optional 'hint' argument here has been used
# to tell SymPy how to solve the ODE. However, it is usually
# smart enough to work it out for itself.
solution = dsolve(ode, y(x), hint='separable')
print "The solution to ODE #5 is: ", solution

###### INTEGRATION FACTOR ######
###### Lecture 7, slide 23 ######
x = Symbol('x') # Independent variable
y = Function('y') # Dependent variable y(x)
# The ODE we wish to solve.
ode = diff(y(x),x) - 2*x + 2*x*y(x)
print "\nODE #6:"
pprint(ode)
# Solve the ode for function y(x).using separation of variables
solution = dsolve(ode, y(x))
print "The solution to ODE #6 is: ", solution


###### APPLICATION: RADIOACTIVE DECAY ######
###### Lecture 7, slide 26 ######
t = Symbol('t') # Independent variable
N = Function('N') # Dependent variable N(t)
l = Symbol('l') # Constant
# The ODE we wish to solve.
ode = diff(N(t),t) + l*N(t)
print "\nODE #7:"
pprint(ode)
solution = dsolve(ode, N(t))
print "The solution to ODE #7 is: ", solution


###### APPLICATION: PARTICLE SETTLING ######
###### Lecture 7, slide 31 ######
t = Symbol('t') # Independent variable - time
v = Function('v') # Dependent variable v(t) - the particle velocity
# Physical constants
rho_f = Symbol('rho_f') # Fluid density
rho_p = Symbol('rho_p') # Particle density
eta = Symbol('eta') # Viscosity
g = Symbol('g') # Gravitational acceleration
a = Symbol('a') # Particle radius
# The ODE we wish to solve.
ode = diff(v(t),t) - ((rho_p - rho_f)/rho_p)*g + (9*eta/(2*(a**2)*rho_p))*v(t)
print "\nODE #8:"
pprint(ode)
solution = dsolve(ode, v(t))
print "The solution to ODE #8 is: ", solution

