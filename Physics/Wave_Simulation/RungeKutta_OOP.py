# Class for housing RungeKutta simulation materials.
# Im trying to keep it as a somewhat generic template.
#
# 25 Nov. 2023

import numpy as np

class RungeKutta:

    def __init__(self, wave_object, time_step_size, testing=False):# Shortened notation
        self.wo = wave_object

        #self.y = 0
        #self.v_y = 0
        self.dt = time_step_size

        # Systems constants/parameters
        #self.c = 0
        #self.k = 0
        #self.mass = 0
        #self.resting_length = 0
        #self.spring_starting_position = 0

        # Number of springs in the system
        self.N = self.wo.number_of_springs

        self.testing = testing


    def main(self, n):
        wo_1 = self.wo.spring_list[n]

        self.y = wo_1.y_position
        self.v_y = wo_1.y_velocity
        
        
        # Systems constants/parameters
        self.origin = wo_1.starting_origin_of_spring
        self.c = wo_1.damping_coefficient
        self.k = wo_1.spring_constant
        self.mass = wo_1.mass
        self.resting_length = wo_1.resting_length




        # Velocity update doesnt use updated position values immediately, but uses the same
        # values that the position calculation had when it started.
        # Then updates both at the conclusion of their respective calculations.
        self.y_place_holder = 0
        self.v_y_place_holder = 0

        self.y_place_holder = ((self.dt/6.0) * (self.k1_y(n) + 2*self.k2_y(n) + 2*self.k3_y(n) + self.k4_y(n)))
        self.v_y_place_holder = ((self.dt/6.0) * (self.k1_vy(n) + 2*self.k2_vy(n) + 2*self.k3_vy(n) + self.k4_vy(n)))
       
        self.y += (self.y_place_holder)
        self.v_y += self.v_y_place_holder

        return self.y, self.v_y



    def k1_y(self, i):
        return self.v_y

    def k1_vy(self, i):
        #print("BEEP:", self.c, "; ", self.mass, "; ", self.v_y, "; ", self.wo.spring_list[i].x_position)
        force_term = self.force(i) / self.mass
        velocity_term = - (self.c / self.mass) * self.v_y
        position_term = - (self.k / self.mass) * (self.y - self.resting_length)

        return force_term + velocity_term + position_term


    def k2_y(self, i):
        return self.v_y + self.k1_vy(i)*(self.dt/2.0)
    def k2_vy(self, i):
        #print("HERE")
        force_term = self.force(i) / self.mass
        velocity_term = - (self.c / self.mass) * (self.v_y + self.k1_vy(i)*(self.dt/2.0))
        position_term = - (self.k / self.mass) * (self.y - self.resting_length + self.k1_y(i)*(self.dt/2.0))

        return force_term + velocity_term + position_term


    def k3_y(self, i):
        return self.v_y + (self.dt/2.0) * self.k2_vy(i)
    def k3_vy(self, i):
        force_term = self.force(i) / self.mass
        velocity_term = - (self.c / self.mass) * (self.v_y + self.k2_vy(i)*(self.dt/2.0))
        position_term = - (self.k / self.mass) * (self.y - self.resting_length + self.k2_y(i)*(self.dt/2.0))

        return force_term + velocity_term + position_term


    def k4_y(self, i):
        return self.v_y + self.dt * self.k3_vy(i)
    def k4_vy(self, i):
        force_term = self.force(i) / self.mass
        velocity_term = - (self.c / self.mass) * (self.v_y + self.dt*self.k3_vy(i))
        position_term = - (self.k / self.mass) * (self.y - self.resting_length + self.dt*self.k3_y(i))

        return force_term + velocity_term + position_term


    def force(self, spot):
        previous_spring = self.wo.spring_list[spot-1]


        if self.testing:
            return 0
        else:
            #diff = self.y[spot-1] - self.y[spot+1]
            #return (diff - self.y[spot])
            #
            # 'p            rint(previous_spring.get_y_position() - self.wo.spring_list[spot].resting_length)
            return (previous_spring.get_y_position() - self.wo.spring_list[spot].resting_length)