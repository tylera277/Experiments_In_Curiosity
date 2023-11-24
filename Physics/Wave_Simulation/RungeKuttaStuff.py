
import numpy as np

class RungeKutta:

    def __init__(self, y, v_y, dt, c, k, mass, N, resting_length,
                 testing):
        self.y = y
        self.v_y = v_y
        self.dt = dt

        # Systems constants/parameters
        self.c = c
        self.k = k
        self.mass = mass
        self.resting_length = resting_length

        # Number of springs in the system
        self.N = N

        self.testing = testing
    def main(self, n):
        # Velocity update doesnt use updated position values immediately, but uses the same
        # values that the position calculation had when it started.
        # Then updates both at the conclusion of their respective calculations
        self.y_place_holder = np.zeros(self.N)
        self.v_y_place_holder = np.zeros(self.N)

        self.y_place_holder[n] = ((self.dt/6.0) * (self.k1_y(n) + 2*self.k2_y(n) + 2*self.k3_y(n) + self.k4_y(n)))

        self.v_y_place_holder[n] = ((self.dt/6.0) * (self.k1_vy(n) + 2*self.k2_vy(n) + 2*self.k3_vy(n) + self.k4_vy(n)))


        self.y += self.y_place_holder
        self.v_y += self.v_y_place_holder

        return self.y[n], self.v_y[n]

    # single driven oscillator
    def k1_y(self, i):
        return self.v_y[i]


    def k1_vy(self, i):
        force_term = self.force(i) / self.mass
        velocity_term = - (self.c / self.mass) * self.v_y[i]
        position_term = - (self.k / self.mass) * (self.y[i] - self.resting_length[i])

        return force_term + velocity_term + position_term


    def k2_y(self, i):
        return self.v_y[i] + self.k1_vy(i)*(self.dt/2.0)
    def k2_vy(self, i):
        force_term = self.force(i) / self.mass
        velocity_term = - (self.c / self.mass) * (self.v_y[i] + self.k1_vy(i)*(self.dt/2.0))
        position_term = - (self.k / self.mass) * (self.y[i] - self.resting_length[i] + self.k1_y(i)*(self.dt/2.0))

        return force_term + velocity_term + position_term


    def k3_y(self, i):
        return self.v_y[i] + (self.dt/2.0) * self.k2_vy(i)
    def k3_vy(self, i):
        force_term = self.force(i) / self.mass
        velocity_term = - (self.c / self.mass) * (self.v_y[i] + self.k2_vy(i)*(self.dt/2.0))
        position_term = - (self.k / self.mass) * (self.y[i] + self.k2_y(i)*(self.dt/2.0))

        return force_term + velocity_term + position_term


    def k4_y(self, i):
        return self.v_y[i] + self.dt * self.k3_vy(i)
    def k4_vy(self, i):
        force_term = self.force(i) / self.mass
        velocity_term = - (self.c / self.mass) * (self.v_y[i] + self.dt*self.k3_vy(i))
        position_term = - (self.k / self.mass) * (self.y[i] + self.dt*self.k3_y(i))

        return force_term + velocity_term + position_term


    def force(self, spot):

        if self.testing:
            return 0
        else:
            #diff = self.y[spot-1] - self.y[spot+1]
            #return (diff - self.y[spot])
            return (self.y[spot - 1] - self.resting_length[spot])

