#!usr/bin/env python
import numpy as np

numParticle = 3
xb = np.array([0.0, 0.0, 0.0])
xa = np.array([-1.0, -1.0, 0.0])
xc = np.array([1.0, -1.0, 0.0])

xg = (xa + xb + xc)/3

arm_len = np.array([1.0, 1.0])

torque = 1.0
