from testing_resources.common_resources import time_function, Profiling_Case
import traceback

def fibonacci_run_case(base_function, sample_solution_function, student_function, n):
    """
    Runs a test case for the Fibonacci project.

    Args:
        base_function (function): The base function to compare against.
        sample_solution_function (function): The sample solution function to compare against.
        student_function (function): The student's function to test.
        n (int): The fibonacci number to find.

    Returns:
        Profiling_Case: An object representing the result of the test case, including timing information and success status.
    """
    case_name = f'Finding fibonacci {n}'

    # no need to check result of base/sample so just grab time
    base_time = time_function(base_function, n)[0]
    sample_solution_time = time_function(sample_solution_function, n)[0]

    # student function may raise exc so try it
    result = None
    try:
        student_solution_time, result = time_function(student_function, n)
    except Exception as e:
        print(f'Your code raised the following exception {n}:')
        traceback.print_exception(type(e), e, e.__traceback__)
        return Profiling_Case(case_name, base_time, sample_solution_time, False)
    
    
    if result != actual(n):
        print(f'Your solution found {result}, but it should have found {actual(n)}.')
        return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)
    else:
        return Profiling_Case(case_name, base_time, sample_solution_time, True, student_solution_time)

actual = lambda x: x if x<2 else (lambda a,b,x: [b:= a+(a:=b) for _ in range(2,x + 1)] and b)(0,1,x)
