import numpy as np
import math
from numpy import sin, cos ,pi

a = np.array([-1,  -1, 0])
b = np.array([ 0,   0, 0])
c = np.array([ 1, - 1 ,0])

vector = np.ndarray(((3,3,3)))
pos = np.stack([a,b,c])
for i in range(3):
    for j in range(3):
        vector[i][j] = pos[j] - pos[i]
        
print(vector)
argument = np.array(2)
argument1 = math.atan2(vector[1][0][1],vector[1][0][0])
argument2 = math.atan2(vector[1][2][1],vector[1][2][0])

theta = argument1 - argument2

print(theta)
rad_theta = np.rad2deg(theta)
rad_argument1 = np.rad2deg(argument1)
rad_argument2 = np.rad2deg(argument2)
"""
print(rad_theta)
print(rad_argument1)
print(rad_argument2)
"""
z = np.cross(vector[1][0], vector[1][2])
#print(z[2])
torque =  1

force = np.zeros((3,3))
if torque > 0:
    tmp1 =  vector[1][0][0] 
    tmp2 = -vector[1][0][1] 
    force[0][0] = tmp2
    force[0][1] = tmp1

    tmp1 = -vector[1][2][0] 
    tmp2 =  vector[1][2][1] 
    force[2][0] = tmp2
    force[2][1] = tmp1

elif torque < 0:
    tmp1 = -vector[1][0][0] 
    tmp2 =  vector[1][0][1] 
    force[0][0] = tmp2
    force[0][1] = tmp1

    tmp1 = -vector[1][2][0] 
    tmp2 =  vector[1][2][1] 
    force[2][0] = tmp2
    force[2][1] = tmp1

force[1] = -force[0] - force[2]

print(force)

