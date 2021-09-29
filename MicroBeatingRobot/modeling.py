#!/usr/bin/env python

import constant as c
import numpy as np
from numpy import einsum 
from numpy import linalg as LA
from numpy import sin, cos, pi


"""
class initial_position(object):
    
    def __init__(self):   
        numparticle = 3
        self.xa = np.array([0.0, 0.0, 0.0])
        self.xb = np.array([-1.0,-1.0,0.0])
        self.xc = np.array([1.0,1.0,0.0])
   
        self.xg = (self.xa + self.xb + self.xc)/3.0 
    
"""

class Particle():
    
    def __init__(self):
       self.position = np.stack([c.xa, c.xb, c.xc])
       self.iter = 0
       self.vector = np.zeros(((c.numParticle, c.numParticle, 3)))


    def get_vector(self, numParticle):
        self.vector_norm = np.empty((numParticle, numParticle))
        self.unit_vector = np.empty(((numParticle, numParticle, 3)))
        
        for i in range(numParticle):
            for j in range(numParticle):
                self.vector[i][j] = self.position[j] - self.position[i]

                self.vector_norm[i][j] = LA.norm(self.vector[i][j])

                if (self.vector_norm[i][j] == 0):
                    self.unit_vector[i][j] = 0
                else:
                    self.unit_vector[i][j] = self.vector[i][j] / self.vector_norm[i][j]


        print("vector norm : '\n'" , self.vector_norm)
        print("vector : '\n'" , self.vector)
        print("vector unit : '\n'" , self.unit_vector)

                        
        
        







if __name__ == "__main__":
    particle = Particle()
    particle.get_vector(c.numParticle)   
