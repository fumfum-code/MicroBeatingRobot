#!/usr/bin/env python

import constant as c
import pandas as pd
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
       self.displacement = np.zeros(3)

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

        for i in range(numParticle-1):
            c.arm_len[i] = self.vector_norm[i][i+1]


 
        #print("vector norm : '\n'" , self.vector_norm)
        #print("vector unit : '\n'" , self.unit_vector)
        print('\033[46m' + "arm length : " + '\033[0m' , c.arm_len)

                        
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
        memo_force = np.zeros((3,3))
        for i in range(1,numParticle-1):
            if torque[i] > 0:
                tmp1 =  abs(torque[i]) * self.unit_vector[i][i-1][0] #vector x position
                tmp2 = -abs(torque[i]) * self.unit_vector[i][i-1][1] #vector y position
               
                memo_force[0][0] = tmp2
                memo_force[0][1] = tmp1
                

                self.force_active[i-1][0] += tmp2 #force x
                self.force_active[i-1][1] += tmp1 #force y
                                
                tmp1 = -abs(torque[i]) * self.unit_vector[i][i+1][0] #vector x position
                tmp2 =  abs(torque[i]) * self.unit_vector[i][i+1][1] #vector y position
                self.force_active[i+1][0] += tmp2 #force x
                self.force_active[i+1][1] += tmp1 #force y
                
                memo_force[2][0] = tmp2
                memo_force[2][1] = tmp1
                
                self.force_active[i] += - memo_force[0] - memo_force[2]
            
            elif torque[i] < 0:
                tmp1 = -abs(torque[i]) * self.unit_vector[i][i-1][0] #vector x position
                tmp2 =  abs(torque[i]) * self.unit_vector[i][i-1][1] #vector y position
                self.force_active[i-1][0] += tmp2 #force x
                self.force_active[i-1][1] += tmp1 #force y
                        
                memo_force[0][0] = tmp2
                memo_force[0][1] = tmp1
                
                tmp1 =  abs(torque[i]) * self.unit_vector[i][i+1][0] #vector x position
                tmp2 = -abs(torque[i]) * self.unit_vector[i][i+1][1] #vector y position
                self.force_active[i+1][0] += tmp2 #force x
                self.force_active[i+1][1] += tmp1 #force y

                
                memo_force[2][0] = tmp2
                memo_force[2][1] = tmp1

            
                self.force_active[i] += -memo_force[0] - memo_force[2]
            else:
                self.force_active[i-1] += 0
                self.force_active[i+1] += 0
                self.force_active[i]   += 0


        #print("check force_active free :", np.sum(self.force_active,axis = 0))


    def get_force_passive(self,numParticle):
        self.force_passive = np.zeros((numParticle,3))

        for i in range(numParticle-1):
            self.force_passive[i]     += -1*c.alpha*(self.vector_norm[i][i+1]/c.arm_len_init[i] - 1)*self.unit_vector[i][i+1]
            self.force_passive[i+1]   += -1*c.alpha*(self.vector_norm[i][i+1]/c.arm_len_init[i] - 1)*self.unit_vector[i+1][i]

    def get_total_force(self, numParticle):
        self.force_total = np.zeros((numParticle,3))
        self.force_total = self.force_active + self.force_passive
        #print('\033[46m' + "force total :" + '\033[0m' + '\n', self.force_total)
        print('\033[46m' + "check force free :" + '\033[0m',np.sum(self.force_total, axis = 0))

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
    

    def check_displacement(self, position):
        centroid = np.sum(position,axis = 0)
        self.displacement = np.concatenate([self.displacement, centroid], axis = 0)
        

    def output(self,iter, angle):
        fig, ax = plt.subplots()
        ax.set_xlim([-2,4])
        ax.set_ylim([-4,4])
        ax.set_title("MicroRobot beating model in stokes flow torque:{:.04f} and {:.04f} ".format(c.torque[1],c.torque[2])) 
        position = self.position.T
        plt.plot(position[0],position[1],zorder = 1)
        plt.scatter(position[0],position[1],zorder = 2, color = 'r')
        plt.scatter(position[0][2],position[1][2],zorder = 3, color = 'g')
        fig.savefig('result/result%6d.png' %iter , format = 'png')

    
    def data_set(self,roop,displacement):
        displacement = displacement.reshape(roop+1,3)
        df = pd.DataFrame(data = displacement, columns = ["displacement_x","displacement_y","displacement_z"])
        df['step'] = np.array(range(c.roop+1))            
        df.to_csv('Databank/data_displacement.csv',index = False)
        print(df)
