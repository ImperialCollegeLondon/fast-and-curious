from testing_resources.common_resources import time_function, Profiling_Case
import traceback

def projectiles_run_case(base_function, sample_solution_function, student_function, mass, velocity, distance, drag_coefficient, cross_section_area, correct_angle):
    """
    Runs a test case for the projectiles project.
    Args:
        base_function (function): The base function to compare against.
        sample_solution_function (function): The sample solution function to compare against.
        student_function (function): The student's function to test.
        mass (float): The mass of the projectile in kg.
        velocity (float): The velocity of the projectile in m/s.
        distance (float): The distance to the target in m.
        drag_coefficient (float): The drag coefficient of the projectile.
        cross_section_area (float): The cross-sectional area of the projectile in m^2.
        correct_angle (float): The correct launch angle in degrees.
    """

    # Set the name of the test case
    case_name = f'Calculating the launch angle for a projectile with a mass of {mass}kg, a velocity of {velocity}m/s, a target distance of {distance}m, a drag coefficient of {drag_coefficient}, and a cross-sectional area of {cross_section_area}m^2 to hit a target at {distance}m'

    # Measure the time taken by the base function to find primes
    base_time = time_function(base_function, mass, velocity, distance, drag_coefficient, cross_section_area)[0]

    # Measure the time taken by the sample solution function to find primes
    sample_solution_time = time_function(sample_solution_function, mass, velocity, distance, drag_coefficient, cross_section_area)[0]

    try:
        # Measure the time taken by the student's function to find primes
        student_solution_time, student_angle = time_function(student_function, mass, velocity, distance, drag_coefficient, cross_section_area)
    except Exception as e:
        # If an exception is raised by the student's function, catch it, print the exception and return a failed test case
        print(f'Your code raised the following exception when asked to calculate the launch angle for a projectile with a mass of {mass}kg, a velocity of {velocity}m/s, a target distance of {distance}m, a drag coefficient of {drag_coefficient}, and a cross-sectional area of {cross_section_area}m^2 to hit a target at {distance}m:')
        traceback.print_exception(type(e), e, e.__traceback__)
        return Profiling_Case(case_name, base_time, sample_solution_time, False)

    try:
        student_angle = float(student_angle)
    except TypeError:
        # If the angle returned by the student's function cannot be converted to a float, print an error message and return a failed test case
        print(f'Your code did not return a number when asked to calculate the launch angle for a projectile with a mass of {mass}kg, a velocity of {velocity}m/s, a target distance of {distance}m, a drag coefficient of {drag_coefficient}, and a cross-sectional area of {cross_section_area}m^2 to hit a target at {distance}m.')
        return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)
    except ValueError:
        # If the angle returned by the student's function cannot be converted to a float, print an error message and return a failed test case
        print(f'Your code did not return a number when asked to calculate the launch angle for a projectile with a mass of {mass}kg, a velocity of {velocity}m/s, a target distance of {distance}m, a drag coefficient of {drag_coefficient}, and a cross-sectional area of {cross_section_area}m^2 to hit a target at {distance} m.')
        return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)
    
    if abs(student_angle - correct_angle) <= 0.1:
        return Profiling_Case(case_name, base_time, sample_solution_time, True, student_solution_time)
    else:
        print(f'Your code returned an angle of {student_angle} degrees when asked to calculate the launch angle for a projectile with a mass of {mass}kg, a velocity of {velocity}m/s, a target distance of {distance}m, a drag coefficient of {drag_coefficient}, and a cross-sectional area of {cross_section_area}m^2 to hit a target at {distance} m. This was not within 0.1 degree of the correct angle of {correct_angle} degrees.')
        return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)
