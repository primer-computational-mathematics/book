# Code taken from
# https://stackoverflow.com/questions/932222/implementing-the-koch-curve

import numpy as np

angles = [np.deg2rad(60*x) for x in range(6)]
sines = [np.sin(x) for x in angles]
cosin = [np.cos(x) for x in angles]

def L(angle, coords, jump):
    return (angle + 1) % 6
def R(angle, coords, jump):
    return (angle + 4) % 6
def F(angle, coords, jump):
    coords.append(
        (coords[-1][0] + jump * cosin[angle],
         coords[-1][1] + jump * sines[angle]))
    return angle

decode = dict(L=L, R=R, F=F)

def grow(steps, length=200, startPos=(0,0)):
    pathcodes="F"
    for i in np.arange(steps):
        pathcodes = pathcodes.replace("F", "FLFRFLF")

    jump = float(length) / (3 ** steps)
    coords = [startPos]
    angle = 0

    for move in pathcodes:
        angle = decode[move](angle, coords, jump)

    return coords