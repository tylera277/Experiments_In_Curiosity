

import numpy as np


class Wave:

    import numpy as np

    def __init__(self, *args):
        self.number_of_springs, self.distance_btwn_points, \
        self.spring_constant, self.mass, self.standard_length_of_spring, \
        self.damping_coefficient = \
        args[0][0], args[0][1], args[0][2], args[0][3], args[0][4], args[0][5]
    

        self.total_x_length = self.distance_btwn_points * self.number_of_springs

        self.y_position = np.zeros(self.number_of_springs)
        self.y_velocity = np.zeros(self.number_of_springs)
        self.x_position = np.linspace(0, self.total_x_length, self.number_of_springs)
        self.resting_length = np.ones(self.number_of_springs)

        # Not needed at the moment
        #self.x_velocity = np.zeros(number_of_springs)