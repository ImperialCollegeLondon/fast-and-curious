from testing_resources.common_resources import time_function, Profiling_Case
import traceback

def five_numbers_run_case(base_function, sample_solution_function, student_function, n, median=7, mode_=8, range_=5):
    """
    Run a test case for the Uncertain Cuboids Project.

    Args:
        base_function (function): The base function to generate all five numbers stasifying the median, mode and range.
        sample_solution_function (function): The sample solution function to generate all five numbers stasifying the median, mode and range.
        student_function (function): The student's function to generate all five numbers stasifying the median, mode and range.
        median (int): The median of each list of five numbers, fixed to 7.
        mode_ (int): The mode of each list of five numbers, fixed to 8.
        range_ (int): The range of each list of five numbers, fixed to 5

    Returns:
        Profiling_Case: An object representing the result of the test case.
    """

    # Define the name of the test case
    case_name = f'All five numbers with median {median}, mode {mode_}, range {range_}'

    # Measure the time taken by the base function
    base_time = time_function(base_function, n, median, mode_, range_)[0]

    # Measure the time taken by the sample solution function
    sample_solution_time = time_function(sample_solution_function, n, median, mode_, range_)[0]

    try:
        # Measure the time taken by the student's function and get the results
        student_solution_time, student_results = time_function(student_function, n, median, mode_, range_)
    except Exception as e:
        # Catch any exceptions raised by the student's function, print the exception, and return a failed test case
        print(f'Your code raised the following exception when asked to find all five numbers with median {median}, mode {mode_}, range {range_}:')
        traceback.print_exception(type(e), e, e.__traceback__)
        return Profiling_Case(case_name, base_time, sample_solution_time, False)
    
    if not isinstance(student_results, tuple) or len(student_results) != 3:
        # Check if the student's function returned the expected number of results
        print(f'Your function did not return Three values when asked to find all five numbers with median {median}, mode {mode_}, range {range_}')
        return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)
    
    #student_mean, student_std = student_results

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

    
    