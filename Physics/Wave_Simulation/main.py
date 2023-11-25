# Program for finding the position of Neptune from Uranus's
# orbit anomalies

import matplotlib
matplotlib.use("TkAgg")
import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


from RungeKuttaStuff import RungeKutta
from SupportFunctions import resting_length_initialize

# User Chosen Parameters
number_of_springs = 40
time_step_size = 0.1
distance_btwn_points = 0.1
spring_constant = 1
mass = 0.1
standard_length_of_spring = 1
damping_coefficient = math.sqrt(4 * mass * spring_constant) # Critically damped condition

# Plot parameters
total_x_length = distance_btwn_points * number_of_springs

# Initializing Needed Vectors, with an initial condition
y_velocity = np.zeros(number_of_springs)
x_position = np.linspace(0, total_x_length, number_of_springs)
x_velocity = np.zeros(number_of_springs)
resting_length = np.ones(number_of_springs)

# Changing the resting lengths of the springs so they get shorter
# the closer they get to the end of the line of springs.
# The main test of my experiment
resting_length = resting_length_initialize(resting_length=resting_length,
                                           number_of_springs=number_of_springs,
                                           standard_length=standard_length_of_spring)

print(resting_length)
y_position = np.zeros(number_of_springs) + resting_length

rk = RungeKutta(y_position, y_velocity,
                time_step_size,
                damping_coefficient, spring_constant, mass, number_of_springs,
                resting_length, testing=False )


# Main loop area
t = 0
dt = 0.1
t_end = 10
spring_two = []


# Create a figure and axis
fig, ax = plt.subplots()
points, = ax.plot(x_position[:], y_position[:], 'o')

# Set plot limits
ax.set_xlim(0, total_x_length)
ax.set_ylim(-10, 10)


def update(frame):

    #print(frame)

    if frame < 30:
        y_velocity[0] = 20 * math.sin(2 * math.pi * frame * (1/30))
    else:
        y_velocity[0] = 0
        y_position[0] = 0

    y_position[0], y_velocity[0] = rk.main(0)
    for spring in range(1, number_of_springs-1, 1):
        y_position[spring], y_velocity[spring] = rk.main(spring)


    # Update the plot with new positions
    points.set_data(x_position[0:number_of_springs - 1], y_position[0:number_of_springs-1])

    return points,


ani = FuncAnimation(fig, update, frames=200, interval=100,
                    blit=False, repeat=False)
plt.show()
