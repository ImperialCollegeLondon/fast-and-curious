import math

class ProjectResults:
    def __init__(self, project_name, project_description):
        self.project_name = project_name
        self.project_description = project_description
        self._cases = []

    def print_results(self):
        print(f'Project: {self.project_name}')
        print(f'Description: {self.project_description}')

        print_major_division()

        for case in self.cases:
            case.print_results(case == self.cases[-1])

        print_minor_division()
        print(f'Average Points: {format_number(self.points)} for Case "{self.project_name}"')

    def add_case(self, case):
        self._cases.append(case)
        self.calculate_points()

    def calculate_points(self):
        self.points = sum([case.points for case in self.cases]) / len(self.cases)

    @property
    def cases(self):
        return self._cases

class Profiling_Case():
    def __init__(self, case_description, base_time, sample_solution_time, student_success, student_time=0):
        self.case_description = case_description
        self.base_time = base_time
        self.sample_solution_time = sample_solution_time
        self.student_success = student_success
        self.student_time = student_time
        if student_success:
            self.points = max(math.log10(self.base_time / self.student_time), 0)
        else:
            self.points = 0

    def print_results(self, last=False):
        print(f'Case: {self.case_description}')
        print(f'Base Time: {format_number(self.base_time)}s')
        print(f'Sample Solution Time: {format_number(self.sample_solution_time)}s')
        print(f'Your Success: {self.student_success}')
        print(f'Your Time: {format_number(self.student_time)}s')
        print(f'Points: {format_number(self.points)}')

        if not last:
            print_minor_division()

def format_number(number):
    if number > 1e-3:
        return '{:.4f}'.format(number)
    else:
        return '{:.4e}'.format(number)

def print_minor_division():
    print('-----------------------------------')

def print_major_division():
    print('===================================')

def time_function(func, *args):
    import time
    start = time.time()
    results = func(*args)
    end = time.time()
    return end - start, results