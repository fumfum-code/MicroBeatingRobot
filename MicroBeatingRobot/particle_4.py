#!usr/bin/env python
import numpy as np

numParticle = 4
I           = np.eye(3)
DT          = 0.001
roop        = 20000

#omega       = 0.3
#K           = 10

beta        = 0.3
K_star      = 5.0
frec        = 0.015
a_star      = 1.0

xb = np.array([0.0, 0.0, 0.0])
xa = np.array([-1.0, -1.0, 0.0])
xc = np.array([1.0, -1.0, 0.0])
xd = np.array([2.0, 0.0, 0.0])

position = np.stack([xa,xb,xc,xd])
xg = (xa + xb + xc) /3

arm_len_init = np.array([1.0, 1.0, 1.0])
arm_len = np.array([1.0, 1.0 , 1.0])

torque  = np.array([0.0, 1.0, 1.0, 0.0])

torque_abs  = np.array([0.0, 1.0, 1.0, 0.0])

