#!/usr/bin/env python 

## Maths Methods 1
## Lecture 5 (Eigenvalues)

## In this file, variable names use the following prefix convention:
## 's' (e.g. sDotProduct) means the variable is a scalar
## 'v' (e.g. vCrossProduct) means the variable is a vector
## 'm' (e.g. mA) means the variable is a matrix

import numpy
import pylab
from math import pi
from sympy import sin, cos, Function, Symbol, diff, integrate, matrices

###### TRANSFORMATION MATRICES ######
###### Lecture 5, slide 9 ######

# Define the transformation matrix in Python using numpy.matrix
mD = numpy.matrix([[1.25, 0],
                  [0, 0.8]])
           
# A list of coordinate vectors in the form [x,y]. 
# These are stored as numpy arrays so we can easily multiply them 
# by the transformation matrix.
vCoordinates = [numpy.array([1, 0]),
               numpy.array([0, 1]),
               numpy.array([-1, 0]),
               numpy.array([0, -1])]

# Take each coordinate and transform it
for i in range(0, len(vCoordinates)):
   # We need to reshape the array so it is conformable
   # (i.e. it is of the right dimension for matrix-vector
   # multiplication). In this case, we need it to be 2 x 1.
   vCoordinates[i] = numpy.reshape(vCoordinates[i], (2,1))
   print mD*vCoordinates[i]
   
sDet = numpy.linalg.det(mD)
sVolStrain = sDet - 1 # The volumetric strain

print "Determinant of D is: %f" % sDet
print "This implies:",
if(sVolStrain == 1):
   print "No volume change"
elif(sVolStrain > 1):
   print "Increase in volume"
elif(sVolStrain > 0 and sVolStrain < 1):
   print "Decrease in volume"
else:
   print "No geological meaning"
   
   
###### EIGENVALUES OF A 2 x 2 MATRIX ######
###### Lecture 5, slide 18 ######
mA = numpy.matrix([[1,4],
                  [1,1]]) 
                  
# A simple way of finding eigenvalues is to use 
# the eigvals function.
sEigValues = numpy.linalg.eigvals(mA)
print "\nThe eigenvalues of mA are: ", sEigValues
             
# Alternatively, we could work out the characteristic polynomial
# for lambda, and then find the roots.
# Computes det(mA - sLambda*mI) and returns a list of scalar coefficients [sX,sY,sZ] for 
# the characteristic polynomial sX*sLambda**2 + sY*sLambda + sZ
sCharacteristicPoly = numpy.poly(mA)
print "\nThe characteristic polynomial of mA is: (%f*lambda**2) + (%f*lambda) + (%f)" % (sCharacteristicPoly[0], sCharacteristicPoly[1], sCharacteristicPoly[2])
# Finds the roots (in this case, these will be the eigenvalues)
sRoots = numpy.roots(sCharacteristicPoly)
print "The roots of the characteristic polynomial are: ", sRoots, "\n"


###### EIGENVECTORS OF A 2 x 2 MATRIX ######
###### Lecture 5, slide 20 ######
mA = numpy.matrix([[1,4],
                  [1,1]]) 
                  
# A simple way of finding eigenvectors is to use 
# the eig function. Note that this gives BOTH the eigenvalues in an array (say 'sEigValues')
# AND eigenvectors in a matrix data type (say 'vEigVectors'). The i-th eigenvector, stored in the column vEigVectors[:,i], 
# corresponds to the eigenvalue stored in sEigValues[i].
(sEigValues, vEigVectors) = numpy.linalg.eig(mA)
for i in range(0, len(sEigValues)):
   print "Eigenvalue #", str(i+1), " is: ", sEigValues[i]
   print "The corresponding eigenvector is: ", vEigVectors[:,i]
print "\n"

###### REPEATED EIGENVALUES ######
###### Lecture 5, slide 24 ######
mA = numpy.matrix([[1,0],
                  [0,1]]) 
#NOTE: Here we could also define mA using numpy.identity(2).

#NOTE: NumPy will give ALL eigenvalues, including the repeated ones.
(sEigValues, vEigVectors) = numpy.linalg.eig(mA)
for i in range(0, len(sEigValues)):
   print "Eigenvalue #", str(i+1), " is: ", sEigValues[i]
   print "The corresponding eigenvector is: ", vEigVectors[:,i]


###### REAL AND COMPLEX EIGENVALUES ######
###### Lecture 5, slide 28 ######
mA = numpy.matrix([[0,1],
                  [-1,0]]) 
# NumPy prints out complex numbers in the form c = a + bj, where j is the imaginary number.
# We can use numpy.real(c) and numpy.imag(c) to print the real and imaginary parts respectively.
sEigValues = numpy.linalg.eigvals(mA) 
print "\nThe eigenvalues of A are: ", sEigValues
print "The real part of the first eigenvalue is: %f" % numpy.real(sEigValues[0])
print "The imaginary part of the first eigenvalue is: %f\n" % numpy.imag(sEigValues[0])


###### EXAMPLE EIGENVALUE PROBLEM ######
###### Lecture 5, slide 30 ######
mM = numpy.matrix([[3,-1],
                  [-1,3]])
(sEigValues, vEigVectors) = numpy.linalg.eig(mA)
for i in range(0, len(sEigValues)):
   print "Eigenvalue #", str(i+1), " is: ", sEigValues[i]
   print "The corresponding eigenvector is: ", vEigVectors[:,i]
print "\n"


###### SYMMETRIC MATRICES ######
###### Lecture 5, slide 31 ######
mNonSymmetric = numpy.matrix([[1,4],
                              [1,1]])
                              
(sEigValues, vEigVectors) = numpy.linalg.eig(mNonSymmetric)
for i in range(0, len(sEigValues)):
   print "Eigenvalue #", str(i+1), " is: ", sEigValues[i]
   print "The corresponding eigenvector is: ", vEigVectors[:,i]
# NOTE 1: Unfortunately, because referencing a column of the matrix vEigVectors
# also returns another matrix data type (essentially a 'sub-matrix' of vEigVectors),
# we cannot use the numpy.dot function (which only operates on vectors/1D arrays).
# Instead, we'll simply use numpy.transpose to perform the dot product instead.
# NOTE 2: could also use numpy.vdot - read the documentation for more info.
print "The dot product of the two eigenvectors is: ", float(numpy.transpose(vEigVectors[:,0])*vEigVectors[:,1])
print "\n"

mSymmetric = numpy.matrix([[3,-1],
                           [-1,3]])
                              
(sEigValues, vEigVectors) = numpy.linalg.eig(mSymmetric)
for i in range(0, len(sEigValues)):
   print "Eigenvalue #", str(i+1), " is: ", sEigValues[i]
   print "The corresponding eigenvector is: ", vEigVectors[:,i]
# The dot product should be zero here, as the two eigenvectors are orthogonal
# for any symmetric matrix. 
print "The dot product of the two eigenvectors is: ", float(numpy.transpose(vEigVectors[:,0])*vEigVectors[:,1])
print "\n"


###### EIGENVALUE PROBLEM FOR A 3 x 3 MATRIX ######
###### Lecture 5, slide 37 ######
mM = numpy.matrix([[2,2,1],
                   [1,3,1],
                   [1,2,2]])
(sEigValues, vEigVectors) = numpy.linalg.eig(mM)
for i in range(0, len(sEigValues)):
   print "Eigenvalue #", str(i+1), " is: ", sEigValues[i]
   print "The corresponding eigenvector is: ", vEigVectors[:,i]
## NOTE: If the values of x1, x2 or x3 are 'free' (i.e. can be chosen arbitrarily to obtain
## an independent eigenvector), NumPy does not necessarily choose values of 0 or 1, which
## is why the eigenvectors printed out here are different from those in your notes.
## They still satisfy the equation (A - lambda*I)x = 0 and are still independent eigenvectors.

