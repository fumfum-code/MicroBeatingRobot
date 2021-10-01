#!usr/bin/env python
import numpy as np

numParticle = 3
I           = np.eye(3)
DT          = 0.3
K           = 5.0

xb = np.array([0.0, 0.0, 0.0])
xa = np.array([-1.0, -1.0, 0.0])
xc = np.array([1.0, -1.0, 0.0])
xd = np.array([2.0, 0.0, 0.0])

position = np.stack([xa,xb,xc])
xg = (xa + xb + xc)/3

arm_len = np.array([1.0, 1.0])

torque  = np.array([0.0, 1.0, 0.0])


