## This cell just imports necessary modules
%pylab notebook
import numpy as np 
import plotly.graph_objs as go

Creating a function that can plot vectors using the Scatter3d() in plotly. In the plots the vectors have a big point to mark the direction.

def vector_plot(tvects,is_vect=True,orig=[0,0,0]):
    """Plot vectors using plotly"""

    if is_vect:
        if not hasattr(orig[0],"__iter__"):
            coords = [[orig,np.sum([orig,v],axis=0)] for v in tvects]
        else:
            coords = [[o,np.sum([o,v],axis=0)] for o,v in zip(orig,tvects)]
    else:
        coords = tvects

    data = []
    for i,c in enumerate(coords):
        X1, Y1, Z1 = zip(c[0])
        X2, Y2, Z2 = zip(c[1])
        vector = go.Scatter3d(x = [X1[0],X2[0]],
                              y = [Y1[0],Y2[0]],
                              z = [Z1[0],Z2[0]],
                              marker = dict(size = [0,5],
                                            color = ['blue'],
                                            line=dict(width=5,
                                                      color='DarkSlateGrey')),
                              name = 'Vector'+str(i+1))
        data.append(vector)

    layout = go.Layout(
             margin = dict(l = 4,
                           r = 4,
                           b = 4,
                           t = 4)
                  )
    fig = go.Figure(data=data,layout=layout)
    fig.show()

# Lecture 1 (Vectors)

This notebook will illustrate how to apply the maths discussed in the lecture using Python.

In these notebooks, we will adopt the following prefix convention when naming variables:

```
's' (e.g. sDotProduct) means the variable is a scalar
'v' (e.g. vCrossProduct) means the variable is a vector
'm' (e.g. mA) means the variable is a matrix
```

# Let's define two vectors, by listing their components
vA = [1, 2, 1]
vB = [-1, 1, 0]

# Convert vA and vB from a list to an array so we can use numpy 
# to perform vector operations on them.
vA = numpy.array(vA)
vB = numpy.array(vB)

print("Plot of vA (blue) and vB (red)")
vector_plot([vA,vB])

###### NULL VECTOR ######
###### Lecture 1, slide 9 ######
# vNull is the null vector (a vector of all zeros,
# created using the zeros function)
vNull = numpy.zeros(3)
print("The null vector is: ", vNull)

###### VECTOR EQUALITY ######
###### Lecture 1, slide 9 ######
# Here we compare vectors vA and vB. This is done element-by-element.
# The .all() function allows us to check that the elements of vA.
# are ALL equal to those of vB. In other words, vA[i] == vB[i] for i = 1, 2, 3
if(numpy.equal(vA,vB).all()):
   print("Vectors vA and vB are equal")
else:
   print("Vectors vA and vB are NOT equal")

###### MULTIPLICATION OF A VECTOR BY A SCALAR ######
###### Lecture 1, slide 9 ######

print("2*vA = ", 2*vA)
print("10*vB = ", 10*vB)

print("Plot of 2*vA (blue) and 10*vB (red)")
vector_plot([2*vA,10*vB])


###### VECTOR ADDITION AND SUBTRACTION ######
###### Lecture 1, slide 10 ######
print("vA + vB = ", vA + vB)
print("vA - vB = ", vA - vB)

print("Plot of vA + vB (blue) and vA - vB (red)")
vector_plot([vA + vB,vA - vB])

###### VECTOR MAGNITUDE ######
###### Lecture 1, slide 7 ######
# Compute the magnitude (aka Euclidean/L2 norm) of vectors vA and vB (to 3 significant figures)
# There are many ways to do this in Python. Try using the sqrt and .dot functions (see below)
# to achieve the same result.
sMagnitude_vA = numpy.linalg.norm(vA, ord=2)
sMagnitude_vB = numpy.linalg.norm(vB, ord=2)
print("Magnitude of vector vA is %.3f" % sMagnitude_vA)
print("Magnitude of vector vB is %.3f" % sMagnitude_vB)

###### DOT PRODUCT ######
###### Lecture 1, slide 15 ######
# Remember: the dot product of two vectors always returns a scalar
sDotProduct_vAvB = numpy.dot(vA,vB)
print("The dot product of vA and vB is %.3f" % sDotProduct_vAvB)

###### ANGLE BETWEEN TWO VECTORS ######
###### Lecture 1, slide 18 ######
# NOTE: arccos is the same as inverse cos
sTheta = numpy.arccos(sDotProduct_vAvB/(sMagnitude_vA*sMagnitude_vB))
print("The angle between vA and vB is %.3f radians (or %.3f degrees)" 
      % (sTheta, sTheta*(180/pi)))


###### CROSS PRODUCT ######
###### Lecture 1, slide 19 ######
# Remember: the cross product of two vectors always returns another vector
print("The cross product of vA and vB is ", numpy.cross(vA,vB))

# Alternatively, we could compute determinants as in slide 22
# Remember: in Python, array indices always start from zero,
# so the x, y and z components have an index of 0, 1 and 2 respectively.
vCrossProduct = [ numpy.linalg.det([[vA[1], vA[2]],
                                [vB[1], vB[2]]]), 
                         
              numpy.linalg.det([[vA[0], vA[2]],
                                [vB[0], vB[2]]]), 
              
              numpy.linalg.det([[vA[0], vA[1]],
                                [vB[0], vB[1]]]) ]
print("The cross product of vA and vB is ", vCrossProduct)

print("Plot of vA (blue),vB (red) and the cross product of vA and vB (green)")

vector_plot([vA,vB,numpy.cross(vA,vB)])

