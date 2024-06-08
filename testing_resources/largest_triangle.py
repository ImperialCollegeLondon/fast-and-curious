from testing_resources.common_resources import time_function, Profiling_Case
import traceback

def largest_triangle_run_case(base_function, sample_solution_function, student_function, n = 500, radius = 50.0, h = 0.0):
    """
    Run a test case for the Largest Inscribed Triangle Project.

    Args:
        base_function (function): The base function to find the largest inscribed triangle in a given circle.
        sample_solution_function (function): The sample solution function to find the largest inscribed triangle in a given circle.
        student_function (function): The student's function to find the largest inscribed triangle in a given circle.
        n (int): steps or gradients
        radius (float): radius of a give circle; preset to 50.
        h (float): height of the largest inscribed triangle in the given circle

    Returns:
        Profiling_Case: An object representing the result of the test case.
    """

    # Define the name of the test case
    case_name = f'The given circle with radius {radius}'

    # Measure the time taken by the base function
    base_time, base_results = time_function(base_function, n, radius, h)

    # Measure the time taken by the sample solution function
    sample_solution_time = time_function(sample_solution_function, n, radius, h)[0]

    try:
        # Measure the time taken by the student's function and get the results
        student_solution_time, student_results = time_function(student_function, n, radius, h)
    except Exception as e:
        # Catch any exceptions raised by the student's function, print the exception, and return a failed test case
        print(f'Your code raised the following exception when asked to find the largest triangle in the given circle with radius {radius}:')
        traceback.print_exception(type(e), e, e.__traceback__)
        return Profiling_Case(case_name, base_time, sample_solution_time, False)
    
    

    #if not isinstance(student_mean, (int, float)) or not isinstance(student_std, (int, float)):
        # Check if the student's function returned the expected types for mean and standard deviation
    #    return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)
    #    print(f'Your function calculate_uncertain_cuboid_statistics did not return two numbers when asked to calculate the mean and standard deviation of the volume of cuboids with a mean length {mean_length}, mean width {mean_width}, mean height {mean_height}, length range {range_length}, width range {range_width}, and height range {range_height} using {n_text} samples')
    
    #if not (acceptable_mean_range[0] <= student_mean <= acceptable_mean_range[1]):
        # Check if the student's function returned a mean volume within the acceptable range
    #    print(f'Your function calculate_uncertain_cuboid_statistics returned a mean volume of {student_mean} when asked to calculate the mean and standard deviation of the volume of cuboids with a mean length {mean_length}, mean width {mean_width}, mean height {mean_height}, length range {range_length}, width range {range_width}, and height range {range_height} using {n_text} samples, but it should have returned a value between {acceptable_mean_range[0]} and {acceptable_mean_range[1]}')
    #    return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)
    
    #if not (acceptable_std_range[0] <= student_std <= acceptable_std_range[1]):
        # Check if the student's function returned a standard deviation within the acceptable range
    #    print(f'Your function calculate_uncertain_cuboid_statistics returned a standard deviation of {student_std} when asked to calculate the mean and standard deviation of the volume of cuboids with a mean length {mean_length}, mean width {mean_width}, mean height {mean_height}, length range {range_length}, width range {range_width}, and height range {range_height} using {n_text} samples, but it should have returned a value between {acceptable_std_range[0]} and {acceptable_std_range[1]}')
    #    return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)
    
    return Profiling_Case(case_name, base_time, sample_solution_time, True, student_solution_time)

    
    