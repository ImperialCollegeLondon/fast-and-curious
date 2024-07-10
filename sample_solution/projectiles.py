import math
from scipy.integrate import solve_ivp
from scipy.optimize import bisect
import numpy as np

def find_launch_angle(mass, velocity, distance, drag_coefficient, cross_section_area):
    '''
    Calculates the launch angle needed to hit a target at a given distance.
    Assumes the required launch angle is between 0 and 45 degrees.
    :param mass: float, The mass of the projectile in kg.
    :param velocity: float, The velocity of the projectile in m/s.
    :param distance: float, The distance to the target in m.
    :param drag_coefficient: float, The drag coefficient of the projectile.
    :param cross_section_area: float, The cross-sectional area of the projectile in m^2.
    :return: float, The launch angle in degrees.
    '''

    def calculate_distance_difference(angle):
        '''
        Calculates the difference between the distance the projectile will travel and the target distance.
        :param angle: float, The launch angle in degrees.
        :return: float, The difference between the projectile range and the target distance.
        '''
        return calculate_distance(mass, velocity, angle, drag_coefficient, cross_section_area) - distance
    
    # Use the bisection method to find the launch angle
    try:
        # If the bisection method converges, return the result
        return bisect(calculate_distance_difference, 0, 45, xtol=0.1)
    except ValueError:
        # If the bisection method does not converge, return None
        return None


def calculate_distance(mass, velocity, angle, drag_coefficient, cross_section_area, dt=0.001):
    '''
    Calculates the distance a projectile will travel given certain parameters.
    :param mass: float, The mass of the projectile in kg.
    :param velocity: float, The velocity of the projectile in m/s.
    :param angle: float, The launch angle in degrees.
    :param drag_coefficient: float, The drag coefficient of the projectile.
    :param cross_section_area: float, The cross-sectional area of the projectile in m^2.
    :return: float, The distance the projectile will travel in m.
    '''
    
    def derivative(t, y):
        '''
        Calculates the derivative of the projectile position.
        :param t: float, The current time.
        :param y: np.array, The current position and velocity of the projectile in the form [x, y, v_x, v_y]
        :return: np.array, The derivative of the projectile position and velocity in the form [dx/dt, dy/dt, dv_x/dt, dv_y/dt]
        '''

        #Initialise the array for the output
        dydt = np.zeros(4)

        # Set the rate of change of x and y
        dydt[0] = y[2]
        dydt[1] = y[3]

        speed = math.sqrt(y[2] ** 2 + y[3] ** 2)
        angle = math.atan(y[3] / y[2])
        deceleration_air_resistance = 1.293 * drag_coefficient * cross_section_area * speed ** 2 / (2 * mass)

        # Update the x and y velocities
        dydt[2] = -deceleration_air_resistance * math.cos(angle)
        dydt[3] = -deceleration_air_resistance * math.sin(angle) - 9.81

        return dydt
    
    def landing_event(t, y):
        '''
        Determines when the projectile hits the ground.
        :param t: float, The current time.
        :param y: np.array, The current position and velocity of the projectile in the form [x, y, v_x, v_y]
        :return: float, The current y position of the projectile.
        '''
        # If the current upward velocity is positive, the projectile has not hit the ground
        if y[3] > 0:
            # Return a non-zero value to stop the solver finishing early
            return 1
        else:
            # Return the height of the projectile
            return y[1]
        
    # Mark the landing event as terminal so the simulation stops when the projectile lands
    landing_event.terminal = True
        
    # Set the initial conditions
    y0 = [0, 0, velocity * math.cos(math.radians(angle)), velocity * math.sin(math.radians(angle))]

    # Set the time span
    # Use a large timespan so the equations won't be stopped early
    t_span = (0, 1e6)

    # Set the events
    results = solve_ivp(derivative, t_span, y0, events=landing_event, dense_output=True)

    # Return the x position of the projectile when it hits the ground
    return results.y[0][-1]

if __name__ == "__main__":
    print(find_launch_angle(0.1, 100, 10000, 0.1, 0.1)) # 45