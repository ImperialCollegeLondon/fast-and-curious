from testing_resources.common_resources import time_function, Profiling_Case
import traceback

def uncertain_cuboids_run_case(base_function, sample_solution_function, student_function, n, n_text, mean_length, mean_width, mean_height, range_length, range_width, range_height, acceptable_mean_range, acceptable_std_range):
    case_name = f'Calculating the mean and standard deviation of the volume of cuboids with a mean length {mean_length}, mean width {mean_width}, mean height {mean_height}, length range {range_length}, width range {range_width}, and height range {range_height} using {n_text} samples'

    base_time = time_function(base_function, n, mean_length, mean_width, mean_height, range_length, range_width, range_height)[0]

    sample_solution_time = time_function(sample_solution_function, n, mean_length, mean_width, mean_height, range_length, range_width, range_height)[0]

    try:
        student_solution_time, student_results = time_function(student_function, n, mean_length, mean_width, mean_height, range_length, range_width, range_height)
    except Exception as e:
        print(f'Your code raised the following exception when asked to calculate the mean and standard deviation of the volume of cuboids with a mean length {mean_length}, mean width {mean_width}, mean height {mean_height}, length range {range_length}, width range {range_width}, and height range {range_height} using {n_text} samples:')
        traceback.print_exception(type(e), e, e.__traceback__)
        return Profiling_Case(case_name, base_time, sample_solution_time, False)
    
    if not isinstance(student_results, tuple) or len(student_results) != 2:
        print(f'Your function calculate_uncertain_cuboid_statistics did not return two values when asked to calculate the mean and standard deviation of the volume of cuboids with a mean length {mean_length}, mean width {mean_width}, mean height {mean_height}, length range {range_length}, width range {range_width}, and height range {range_height} using {n_text} samples')
        return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)
    
    student_mean, student_std = student_results

    if not isinstance(student_mean, (int, float)) or not isinstance(student_std, (int, float)):
        print(f'Your function calculate_uncertain_cuboid_statistics did not return two numbers when asked to calculate the mean and standard deviation of the volume of cuboids with a mean length {mean_length}, mean width {mean_width}, mean height {mean_height}, length range {range_length}, width range {range_width}, and height range {range_height} using {n_text} samples')
        return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)
    
    if not (acceptable_mean_range[0] <= student_mean <= acceptable_mean_range[1]):
        print(f'Your function calculate_uncertain_cuboid_statistics returned a mean volume of {student_mean} when asked to calculate the mean and standard deviation of the volume of cuboids with a mean length {mean_length}, mean width {mean_width}, mean height {mean_height}, length range {range_length}, width range {range_width}, and height range {range_height} using {n_text} samples, but it should have returned a value between {acceptable_mean_range[0]} and {acceptable_mean_range[1]}')
        return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)
    
    if not (acceptable_std_range[0] <= student_std <= acceptable_std_range[1]):
        print(f'Your function calculate_uncertain_cuboid_statistics returned a standard deviation of {student_std} when asked to calculate the mean and standard deviation of the volume of cuboids with a mean length {mean_length}, mean width {mean_width}, mean height {mean_height}, length range {range_length}, width range {range_width}, and height range {range_height} using {n_text} samples, but it should have returned a value between {acceptable_std_range[0]} and {acceptable_std_range[1]}')
        return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)
    
    return Profiling_Case(case_name, base_time, sample_solution_time, True, student_solution_time)

    
    