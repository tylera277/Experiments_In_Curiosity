# A (in theory) simple interface for a user to run the simulation,
# all they need to enter is parameters that they choose.
# The aim is to modularize and tuck away details the user shouldn't
# be concerned with &/or have access to
#
# 25 Nov 2023


###########################################
#############    IMPORTS      #############

import matplotlib
matplotlib.use("TkAgg")
import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from Wave_OOP import Wave
from Simulation_OOP import Simulation


###########################################
###########################################
######   USER-CHOSEN PARAMETERS   #########

    ## Chosen parameters of wave
number_of_springs = 20
distance_btwn_points = 0.1
spring_constant = 1
mass = 0.1
standard_length_of_spring = 1
damping_coefficient = math.sqrt(4 * mass * spring_constant) # Critically damped condition

    ## Chosen parameters of simulation/plot
number_of_frames = 1000
display_time_for_each_frame = 100 #(in milliseconds)
time_step_size_rungeKuttaCalculation = 0.1
total_time_rungeKuttaCalculation = 10
plot_x_axis_range = [0, distance_btwn_points * number_of_springs]
plot_y_axis_range = [-10, 10]
 

    ## Storing in lists to be easily entered into class and functions
wave_parameters = [number_of_springs, distance_btwn_points, \
                   spring_constant, mass, standard_length_of_spring, damping_coefficient]

simulation_parameters = [number_of_frames, display_time_for_each_frame,
                         time_step_size_rungeKuttaCalculation, 
                         total_time_rungeKuttaCalculation, 
                         plot_x_axis_range, plot_y_axis_range]

###########################################
###########################################



# the Wave object which will house
# the specifics/details about the springs themselves.
myWave = Wave(wave_parameters)

# the Simulation object which will be the central
# command for all functions of the dynamics and plotting in regard
# to the spring system
mySimulation = Simulation(myWave, simulation_parameters)

mySimulation.run()