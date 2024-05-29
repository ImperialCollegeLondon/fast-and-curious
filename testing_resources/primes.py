from testing_resources.common_resources import time_function, Profiling_Case
import traceback

def primes_run_case(base_function, sample_solution_function, student_function, n, n_text, reference_file_path):
    """
    Runs a test case for the Primes project.

    Args:
        base_function (function): The base function to compare against.
        sample_solution_function (function): The sample solution function to compare against.
        student_function (function): The student's function to test.
        n (int): The upper limit for finding prime numbers.
        n_text (str): The string representation of the upper limit.
        reference_file_path (str): The file path to the reference file containing the expected prime numbers.

    Returns:
        Profiling_Case: An object representing the result of the test case, including timing information and success status.
    """

    # Set the name of the test case
    case_name = f'Writing primes under {n_text}'

    # Measure the time taken by the base function to find primes
    base_time = time_function(base_function, n, 'testing_resources/primes.txt')[0]

    # Measure the time taken by the sample solution function to find primes
    sample_solution_time = time_function(sample_solution_function, n, 'testing_resources/primes.txt')[0]

    try:
        # Measure the time taken by the student's function to find primes
        student_solution_time = time_function(student_function, n, 'testing_resources/primes.txt')[0]
    except Exception as e:
        # If an exception is raised by the student's function, catch it, print the exception and return a failed test case
        print(f'Your code raised the following exception when asked to find the primes under {n_text}:')
        traceback.print_exception(type(e), e, e.__traceback__)
        return Profiling_Case(case_name, base_time, sample_solution_time, False)

    try:
        # Read the lines from the file created by the student's function
        with open('testing_resources/primes.txt') as file:
            student_lines = file.readlines()
    except FileNotFoundError:
        # If the file is not found, print an error message and return a failed test case
        print(f'Your code did not create a file called "testing_resources/primes.txt" when asked to find the primes under {n_text}.')
        return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)

    try:
        # Convert the lines from the file into a list of integers
        student_primes = [int(line.strip()) for line in student_lines]
    except ValueError:
        # If the lines in the file cannot be converted to integers, print an error message and return a failed test case
        print(f'Your code did not write only integers to the file "primes.txt" when asked to find the primes under {n_text}.')
        return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)

    # Read the lines from the reference file
    with open(reference_file_path) as file:
        reference_lines = file.readlines()

    # Convert the lines from the reference file into a list of integers
    reference_primes = [int(line.strip()) for line in reference_lines]

    if len(student_primes) != len(reference_primes):
        # If the number of primes found by the student's function is different from the reference, print an error message and return a failed test case
        print(f'Your solution found {len(student_primes)} primes, but it should have found {len(reference_primes)} primes.')
        return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)
    else:
        for i in range(len(student_primes)):
            # Loop over each prime
            if student_primes[i] != reference_primes[i]:
                # If a prime found by the student's function is different from the reference, print an error message and return a failed test case
                print(f'The prime on line {i + 1} of your output was {student_primes[i]}, but it should have been {reference_primes[i]}.')
                return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)
        else:
            # If all primes found by the student's function match the reference, return a successful test case
            return Profiling_Case(case_name, base_time, sample_solution_time, True, student_solution_time)
