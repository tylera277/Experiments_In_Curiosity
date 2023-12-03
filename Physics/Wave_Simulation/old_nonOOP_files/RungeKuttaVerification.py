# Verifying my runge kutta simulation code against a known
# solution to verify it is accurately being done

# 23 Nov 2023

import matplotlib
matplotlib.use("TkAgg")
import math

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


from RungeKuttaStuff import RungeKutta


# Parameters
number_of_springs = 1
time_step_size = 0.1
distance_btwn_points = 0.1
spring_constant = 1
mass = 0.1
damping_coefficient = 0

# total_x_length = distance_btwn_points * number_of_springs

# Initializing Needed Vectors, with an initial condition
y_position_pred = np.zeros(number_of_springs)
y_velocity_pred = np.zeros(number_of_springs)
x_position = [0.5]
x_velocity = np.zeros(number_of_springs)
resting_length = np.zeros(number_of_springs)

y_position_act = np.zeros(number_of_springs)



# Main loop area
t = 0
dt = 0.1
t_end = 10

# Initial conditions
y_position_pred[0] = 1
y_velocity_pred[0] = 0

rk = RungeKutta(y=y_position_pred, v_y=y_velocity_pred,
                dt=time_step_size,
                c=damping_coefficient, k=spring_constant, mass=mass,
                N=number_of_springs, resting_length=resting_length,
                testing=True)

# Create a figure and axis
fig, ax = plt.subplots()
points, = ax.plot(x_position[0], y_position_pred[0], 'o')

# Set plot limits
ax.set_xlim(0, 1)
ax.set_ylim(-5, 5)

def position_actual(drag_coeff, mass, spring_coeff, amplitude,
                    time):

    drag_coeff_m = drag_coeff / mass
    spring_coeff_m = spring_coeff / mass

    omega = math.sqrt(spring_coeff_m)
    position = amplitude * math.exp(-drag_coeff_m * time) * math.cos(omega * time)

    return position
def update(frame):
    print(frame)
    y_position_act[0]= position_actual(drag_coeff=damping_coefficient,
                                     mass=mass,
                                     spring_coeff=spring_constant,
                                     amplitude=1,
                                     time=time_step_size)
    y_position_pred[0], y_velocity_pred[0] = rk.main(0)

    #print("BEEP:", y_position_pred[0])
    print("DIFF=", y_position_act[0] - y_position_pred[0])
    # Update the plot with new positions
    #points.set_data(x_position[0], y_position_pred[0])
    points.set_data(x_position[0], y_position_act)

    return points,


ani = FuncAnimation(fig, update, frames=100, interval=100,
                    blit=False, repeat=False)
plt.show()
