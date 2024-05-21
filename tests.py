from testing_resources.common_resources import ProjectResults, print_major_division, format_number
from testing_resources.primes import primes_run_case

def run_tests():
    project_results = []
    project_results.append(test_project_primes())

    total_points = sum([project.points for project in project_results])

    print_major_division()
    print(f'Total Points: {format_number(total_points)}')


def test_project_primes():
    from base.primes import write_primes as base_function
    from sample_solution.primes import write_primes as sample_solution_function
    from student.primes import write_primes as student_function

    project1_results = ProjectResults('Primes', 'Write primes under n to a specified file.')

    project1_results.add_case(primes_run_case(base_function, sample_solution_function, student_function, 1000, '1,000', 'testing_resources/reference_primes_1k.txt'))
    project1_results.add_case(primes_run_case(base_function, sample_solution_function, student_function, 10000, '10,000', 'testing_resources/reference_primes_10k.txt'))

    project1_results.print_results()

    return project1_results


if __name__ == '__main__':
    run_tests()
    