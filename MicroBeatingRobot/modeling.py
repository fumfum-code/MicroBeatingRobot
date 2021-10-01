#!/usr/bin/env python

import constant as c
import matplotlib.pyplot as plt
import numpy as np
from numpy import einsum 
from numpy import linalg as LA
from numpy import sin, cos, pi


class Particle():
    
    def __init__(self):
       self.position = c.position
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
        print("vector unit : '\n'" , self.unit_vector)

                        
    def get_angle(self, u: np.ndarray, v : np.ndarray):
        i = np.inner(u, v)
        n = LA.norm(u) * LA.norm(v)
        c = i /n 
        z = np.cross(u,v)
        if z[2] > 0:
            return np.arccos(np.clip(c, -1.0, 1.0))
        elif z[2] < 0:   
            return 2*pi - np.arccos(np.clip(c, -1.0, 1.0))
                   
        
    def get_argument(self, u: np.ndarray, v: np.ndarray):
        angle1 = math.atan2(u[1], u[0])
        angle2 = math.atan2(v[1], v[0])
        return  angle1 -angle2


    def get_force_active(self,numParticle , torque: np.ndarray):
        
        self.force_active = np.zeros((numParticle,3))
       
        for i in range(1,numParticle-1):
            if torque[i] > 0:
                tmp1 =  self.unit_vector[i][i-1][0] #vector x position
                tmp2 = -self.unit_vector[i][i-1][1] #vector y position
                self.force_active[i-1][0] += tmp2 #force x
                self.force_active[i-1][1] += tmp1 #force y
                        
                tmp1 = -self.unit_vector[i][i+1][0] #vector x position
                tmp2 =  self.unit_vector[i][i+1][1] #vector y position
                self.force_active[i+1][0] += tmp2 #force x
                self.force_active[i+1][1] += tmp1 #force y
                        
                self.force_active[i] = -self.force_active[i-1] - self.force_active[i+1]
            
            elif torque[i] < 0:
                tmp1 = -self.unit_vector[i][i-1][0] #vector x position
                tmp2 =  self.unit_vector[i][i-1][1] #vector y position
                self.force_active[i-1][0] += tmp2 #force x
                self.force_active[i-1][1] += tmp1 #force y
                        
                tmp1 =  self.unit_vector[i][i+1][0] #vector x position
                tmp2 = -self.unit_vector[i][i+1][1] #vector y position
                self.force_active[i+1][0] += tmp2 #force x
                self.force_active[i+1][1] += tmp1 #force y

                self.force_active[i] = -self.force_active[i-1] - self.force_active[i+1]
            
            else:
                self.force_active[i-1] += 0
                self.force_active[i+1] += 0
                self.force_active[i]   += 0

        print("force_active :",self.force_active)


    def get_force_passive(self,numParticle):
        self.force_passive = np.zeros((numParticle,3))

        for i in range(numParticle-1):
            self.force_passive[i]     += -2*c.K*(self.vector_norm[i][i+1] - c.arm_len[i])*self.unit_vector[i][i+1]
            self.force_passive[i+1]   += -2*c.K*(self.vector_norm[i][i+1] - c.arm_len[i])*self.unit_vector[i+1][i]


    def get_total_force(self, numParticle):
        self.force_total = np.zeros((numParticle,3))
        self.force_total = self.force_active + self.force_passive
        print("check force free :",np.sum(self.force_total, axis = 0))

    def calculate_tensor(self, numParticle):
        
        self.ossen_tensor = np.zeros((((numParticle,numParticle,3,3))))
        
        for i in range(numParticle):
            for j in range(numParticle):
                if(self.vector_norm[i][j] == 0):
                    continue
                reshape_r = self.vector[i][j].reshape(3,1)

                tmp = c.I + np.einsum('i,j -> ij', self.vector[i][j],self.vector[i][j])/(self.vector_norm[i][j]**2)
        
                self.ossen_tensor[i][j] = tmp / (8*pi*self.vector_norm[i][j])


    def update(self, numParticle, force):
        self.v = np.zeros((numParticle,3))
        box = np.zeros((numParticle, 3))

        for i in range(numParticle):
            for j in range(numParticle):
                if i == j:
                    box[j] = 0.0
                else:
                    tmp = np.dot(self.ossen_tensor[i][j], force[j].T)
                    box[j] = tmp.T
                self.v[i] = np.sum(box, axis= 0)


        self.position += self.v * c.DT

        print("new position \n :",self.position)


    def output(self,iter, angle):
        fig, ax = plt.subplots()
        ax.set_xlim([-2,4])
        ax.set_ylim([-4,4])
        ax.set_title("MicroRobot beating model in stokes flow angle:%3d" %iter) 
        position = self.position.T
        plt.plot(position[0],position[1],zorder = 1)
        plt.scatter(position[0],position[1],zorder = 2, color = 'r')
        plt.scatter(position[0][2],position[1][2],zorder = 3, color = 'g')
        fig.savefig('result/result%4d.png' %iter , format = 'png')







