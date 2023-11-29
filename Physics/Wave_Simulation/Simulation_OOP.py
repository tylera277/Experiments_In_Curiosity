
# Object which will be the central command for handling 
# the details of actually simulating the waves
#
# 25 Nov 2023

import math

import matplotlib
matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from Wave_OOP import Wave
from RungeKutta_OOP import RungeKutta


class Simulation:

    def __init__(self, wave_object, *args):
        self.wave_object = wave_object
        self.number_of_frames = args[0][0]
        self.display_time = args[0][1]
        self.time_step_size_rungeKuttaCalculation = args[0][2]
        self.total_time_rungeKuttaCalculation = args[0][3]
        self.plot_x_axis_range = args[0][4]
        self.plot_y_axis_range = args[0][5]

    def animation(self):
        pass


    def run(self):

        # The actual calculator object
        rk_sim = RungeKutta(wave_object=self.wave_object,
                            time_step_size=self.time_step_size_rungeKuttaCalculation)




        # Plotting details which I may try to tuck away into its own 
        # object/class in the future

        # Create a figure and axis
        fig, ax = plt.subplots()
        points, = ax.plot(self.wave_object.x_position[:], self.wave_object.y_position[:], 'o')

        # Set plot limits
        ax.set_xlim(self.plot_x_axis_range[0], self.plot_x_axis_range[1])
        ax.set_ylim(self.plot_y_axis_range[0], self.plot_y_axis_range[1])

        def update(frame):


            if frame < 30:
                self.wave_object.y_velocity[0] = 20 * math.sin(2 * math.pi * frame * (1/30))
            else:
                self.wave_object.y_velocity[0] = 0
                self.wave_object.y_position[0] = 0

            self.wave_object.y_position[0], self.wave_object.y_velocity[0] = rk_sim.main(0)

            for spring in range(1, self.wave_object.number_of_springs-1, 1):
                
                self.wave_object.y_position[spring], self.wave_object.y_velocity[spring] = rk_sim.main(spring)


            # Update the plot with new positions
            points.set_data(self.wave_object.x_position[0:self.wave_object.number_of_springs-1], \
                            self.wave_object.y_position[0:self.wave_object.number_of_springs-1])

            return points,


        ani = FuncAnimation(fig, update, frames=self.number_of_frames, interval=self.display_time,
                    blit=False, repeat=False)
        plt.show()
    
        
