#!usr/bin/env python
import numpy as np

numParticle = 4
I           = np.eye(3)
DT          = 0.001
#K           = 10
roop        = 100000
#omega       = 0.3

beta        = 0.3
alpha       = 1.0


xb = np.array([0.0, 0.0, 0.0])
xa = np.array([-1.0, -1.0, 0.0])
xc = np.array([1.0, -1.0, 0.0])
xd = np.array([2.0, 0.0, 0.0])

position = np.stack([xa,xb,xc,xd])
xg = (xa + xb + xc) /3

arm_len_init = np.array([1.0, 1.0, 1.0])
arm_len = np.array([1.0, 1.0 , 1.0])

torque  = np.array([0.0, 1.0, 1.0, 0.0])


