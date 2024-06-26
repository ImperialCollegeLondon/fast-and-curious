import math
import time

class ProjectResults:
    """
    Represents the results of a project.

    Attributes:
        project_name (str): The name of the project.
        project_description (str): The description of the project.
        _cases (list): A list of Case objects representing the test cases for the project.
        points (float): The average points earned for the project.
    """

    def __init__(self, project_name, project_description):
        """
        Initializes a new instance of the ProjectResults class.

        Args:
            project_name (str): The name of the project.
            project_description (str): The description of the project.
        """
        self.project_name = project_name
        self.project_description = project_description
        self._cases = []
        self.points = 0

    def print_results(self):
        """
        Prints the results of the project.

        This method prints the project name, description, and the results of each test case.
        """
        print_major_division()

        print(f'Project: {self.project_name}')
        print(f'Description: {self.project_description}')

        print_major_division()

        for case in self.cases:
            case.print_results(case == self.cases[-1])

        print_minor_division()
        print(f'Average Points: {format_number(self.points)} for Case "{self.project_name}"')

    def add_case(self, case):
        """
        Adds a test case to the project.

        Args:
            case (Case): The test case to add.
        """
        self._cases.append(case)
        self.calculate_points()

    def calculate_points(self):
        """
        Calculates the average points earned for the project.
        """
        if all([case.student_success for case in self.cases]):
            self.points = sum([case.points for case in self.cases]) / len(self.cases)
        else:
            self.points = 0

    @property
    def cases(self):
        """
        Gets the list of test cases for the project.

        Returns:
            list: A list of Case objects representing the test cases for the project.
        """
        return self._cases

class Profiling_Case():
    """
    Represents a profiling case for performance testing.

    Attributes:
        case_description (str): The description of the profiling case.
        base_time (float): The base time for the case (s).
        sample_solution_time (float): The time taken by the sample solution for the case (s).
        student_success (bool): Indicates whether the student's solution was successful for the case (s).
        student_time (float, optional): The time taken by the student's solution for the case. Defaults to 0 (s).
        points (float): The points earned for the case based on the student's performance.
    """

    def __init__(self, case_description, base_time, sample_solution_time, student_success, student_time=0):
        """
        Initializes a new instance of the Profiling_Case class.

        Args:
            case_description (str): The description of the profiling case.
            base_time (float): The base time for the case (s).
            sample_solution_time (float): The time taken by the sample solution for the case (s).
            student_success (bool): Indicates whether the student's solution was successful for the case (s).
            student_time (float, optional): The time taken by the student's solution for the case. Defaults to 0 (s).
        """
        self.case_description = case_description
        self.base_time = base_time
        self.sample_solution_time = sample_solution_time
        self.student_success = student_success
        self.student_time = student_time
        if student_success and self.base_time > 0:
            self.points = max(math.log10(self.base_time / max(self.student_time, self.base_time * 1e-5)), 0)
        else:
            self.points = 0

    def print_results(self, last=False):
        """
        Prints the results of the profiling case.

        Args:
            last (bool, optional): Indicates whether this is the last case. Defaults to False.
        """
        print(f'Case: {self.case_description}')
        print(f'Base Time: {format_number(self.base_time)}s')
        print(f'Sample Solution Time: {format_number(self.sample_solution_time)}s')
        print(f'Your Success: {self.student_success}')
        print(f'Your Time: {format_number(self.student_time)}s')
        print(f'Points: {format_number(self.points)}')

        if not last:
            print_minor_division()

def format_number(number):
    """
    Formats a number for display.

    Args:
        number (float): The number to format.

    Returns:
        str: The formatted number.
    """
    if number > 1e-3:
        return '{:.4f}'.format(number)
    else:
        return '{:.4e}'.format(number)

def print_minor_division():
    '''
    Print a minor division to the console.
    '''
    print('-----------------------------------')

def print_major_division():
    '''
    Print a major division to the console.
    '''
    print('===================================')

def time_function(func, *args):
    """
    Measures the execution time of a function.

    Args:
        func (function): The function to be timed.
        *args: Variable length argument list to be passed to the function.

    Returns:
        tuple: A tuple containing the execution time in seconds and the result of the function.
    """
    start = time.time()
    results = func(*args)
    end = time.time()
    return end - start, results