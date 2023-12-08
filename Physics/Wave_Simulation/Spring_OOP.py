
import numpy as np


class Spring:

    def __init__(self, initial_x_position,
                 initial_y_position, initial_y_velocity,
                 starting_origin_of_spring, 
                 mass,
                 resting_length, spring_starting_position,
                 spring_constant, damping_coefficient):
        
        self.x_position = initial_x_position
        #self.y_position = initial_y_position
        self.y_position = starting_origin_of_spring
        self.y_velocity = initial_y_velocity
        
        self.starting_origin_of_spring = starting_origin_of_spring
        self.mass = mass
        self.resting_length = resting_length
        self.spring_starting_position = spring_starting_position
        self.spring_constant = spring_constant
        self.damping_coefficient = damping_coefficient
    
    def get_x_position(self):
        return self.x_position
    
    def get_y_position(self):
        return self.y_position
    
    def get_y_velocity(self):
        return self.y_velocity

    def set_y_position(self, new_pos):
        self.y_position = new_pos
    
    def set_y_velocity(self, new_vel):
        self.y_velocity = new_vel