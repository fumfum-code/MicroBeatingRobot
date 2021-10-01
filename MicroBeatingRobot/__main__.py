import modeling
import constant as c
import numpy as np 
if __name__ == "__main__":
    angle1 = 90
    angle2 = 90
    particle = modeling.Particle()
    for iter in range(300):
        
        if angle1 > 270:
            c.torque[1] = -1.0
        """
        if angle2 > 270:
            c.torque[2] = -1.0
        """
        if angle1 < 90:
            c.torque[1] =  1.0
        
        """
        if angle2 < 90:
            c.torque[2] =  1.0
        """
 
        print('---now caluculating {} ---'.format(iter))        
         
        particle.output(iter, angle2)
        particle.get_vector(c.numParticle)
        angle1  = np.rad2deg(particle.get_angle(particle.unit_vector[1][0], particle.unit_vector[1][2]))
        #angle2  = np.rad2deg(particle.get_angle(particle.unit_vector[2][1], particle.unit_vector[2][3]))
        print("angle1 :" , angle1)
        #print("angle2 :" , angle2)

        particle.get_force_active(c.numParticle, c.torque)
        particle.get_force_passive(c.numParticle)
        particle.get_total_force(c.numParticle)
        particle.calculate_tensor(c.numParticle)
        particle.update(c.numParticle, particle.force_active)





