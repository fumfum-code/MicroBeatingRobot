import modeling
import constant as c
import numpy as np 
from numpy import sin, cos ,pi


if __name__ == "__main__":
    angle1 = 90
    angle2 = 90
    particle = modeling.Particle()
    for iter in range(c.roop):
        time = c.DT * iter
        
        c.torque[1] = sin(c.beta * time + pi/2)
        c.torque[2] = sin(c.beta * time)

        print('---now caluculating {} --- '.format(iter) )        
        if iter % 100 == 0: 
            particle.output(iter, angle2)
       
        particle.check_displacement(c.position)
        particle.get_vector(c.numParticle)
        
        angle1  = np.rad2deg(particle.get_angle(particle.unit_vector[1][0], particle.unit_vector[1][2]))
        angle2  = np.rad2deg(particle.get_angle(particle.unit_vector[2][1], particle.unit_vector[2][3]))
  
        print("angle1 :" , angle1)
        print("angle2 :" , angle2)

        particle.get_force_active(c.numParticle, c.torque)
        particle.get_force_passive(c.numParticle)
    
        particle.get_total_force(c.numParticle)
        particle.calculate_tensor(c.numParticle)
        particle.update(c.numParticle, particle.force_total)


    particle.data_set(c.roop, particle.displacement)
    
