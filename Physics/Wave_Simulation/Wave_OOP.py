

import numpy as np
from Spring_OOP import Spring

class Wave:

    def __init__(self, *args):

        self.number_of_springs, self.distance_btwn_points, \
        self.spring_constant, self.mass, self.standard_length_of_spring, \
        self.damping_coefficient = \
        args[0][0], args[0][1], args[0][2], args[0][3], args[0][4], args[0][5]

        self.total_x_length = self.distance_btwn_points * self.number_of_springs

        self.x_position = np.linspace(0, self.total_x_length, self.number_of_springs-1)


        # Where all of the spring objects are created.
        self.spring_list = self.create_springs()


        #self.spring_starting_position, self.resting_length = self.initialize_starting_position_base_of_spring()

    
        # Not needed at the moment
        #self.x_velocity = np.zeros(number_of_springs)

    def create_springs(self):
        spring_list = []
        
        
        for spring in range(0, self.number_of_springs-1, 1):

            spring_list.append( Spring(self.x_position[spring], 0, 0, self.mass,
                                      1, 1, self.spring_constant, self.damping_coefficient) )
    
        return spring_list

        
    def initialize_starting_position_base_of_spring(self):

        halfeth_spring = int(self.number_of_springs / 2.0)

        for spring in range(halfeth_spring, self.number_of_springs, 1):
            
            length_value = ((-2 * self.standard_length_of_spring) / self.number_of_springs) * \
                spring + (2 * self.standard_length_of_spring)
                            
            self.resting_length[spring] = self.standard_length_of_spring - length_value
            #self.spring_starting_position[spring] = self.standard_length_of_spring - length_value

        return  self.spring_starting_position, self.resting_length