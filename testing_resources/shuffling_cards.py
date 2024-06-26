from testing_resources.common_resources import time_function, Profiling_Case
import traceback

def shuffling_cards_run_case(base_function, sample_solution_function, student_function, deck_size, instructions, card, actual):
    """
    Runs a test case for the Shuffling Cards project.

    Args:
        base_function (function): The base function to compare against.
        sample_solution_function (function): The sample solution function to compare against.
        student_function (function): The student's function to test.
        n (int): The fibonacci number to find.

    Returns:
        Profiling_Case: An object representing the result of the test case, including timing information and success status.
    """
    case_name = f'Shuffling {deck_size} cards to find {card} after following these instructions: \n{", ".join(instructions)}'

    # check result of base/sample solution
    base_time, base_result = time_function(base_function, deck_size, instructions, card)
    sample_solution_time, sample_result = time_function(sample_solution_function, deck_size, instructions, card)
    assert base_result == sample_result == actual, f'Base function and sample solution do not agree with actual!'

    # student function may raise exc so try it
    result = None
    try:
        student_solution_time, result = time_function(student_function, deck_size, instructions, card)
    except Exception as e:
        print(f'Your code raised the following exception {e}:')
        traceback.print_exception(type(e), e, e.__traceback__)
        return Profiling_Case(case_name, base_time, sample_solution_time, False)
    
    
    if result != actual:
        print(f'Your solution found {result}, but it should have found {actual}.')
        return Profiling_Case(case_name, base_time, sample_solution_time, False, student_solution_time)
    else:
        return Profiling_Case(case_name, base_time, sample_solution_time, True, student_solution_time)
