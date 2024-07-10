import math
import matplotlib.pyplot as plt

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

    # Calculate all the angles to check
    # Every 0.1 degrees from 0 to 45 
    angles = []
    for i in range(451):
        angles.append(i * 0.1)

    # Loop over all possible launch angles
    for angle in angles:
        # For the current angle, calculate the range of the projectile
        projectile_range = calculate_distance(mass, velocity, angle, drag_coefficient, cross_section_area)

        # If the range is greater than the target distance, the current angle will be within 1 degree of the correct angle
        if projectile_range > distance:
            # Return the current angle
            return angle
    else:
        # If no angle is found, return None
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
    
    # Initialise the x and y positions
    x = 0
    y = 0

    # Initialise the x and y velocities
    v_x = velocity * math.cos(math.radians(angle))
    v_y = velocity * math.sin(math.radians(angle))

    # Loop until the projectile hits the ground
    # Each step represents a time interval of dt seconds
    while y >= 0:
        # Update the x and y positions
        x += v_x * dt
        y += v_y * dt

        # Calculate the current speed, angle and rate of deceleration due to air resistance
        speed = math.sqrt(v_x ** 2 + v_y ** 2)
        angle = math.atan(v_y / v_x)
        deceleration_air_resistance = 1.293 * drag_coefficient * cross_section_area * speed ** 2 / (2 * mass)

        # Update the x and y velocities
        v_x -= deceleration_air_resistance * math.cos(angle) * dt
        v_y -= (deceleration_air_resistance * math.sin(angle) + 9.81) * dt

    # The loop has ended, so the projectile hit the ground
    # The x position is the distance the projectile traveled
    return x