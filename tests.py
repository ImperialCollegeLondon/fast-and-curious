from testing_resources.common_resources import ProjectResults, print_minor_division, format_number


def run_tests():
    project_results = []
    project_results.append(test_project_primes(print_project_level_output=False))

    total_points = sum([project.points for project in project_results])

    for project in project_results:
        print(f'{project.project_name}: {format_number(project.points)} points')
        print_minor_division()
    print(f'Total Points: {format_number(total_points)}')


def test_project_primes(print_project_level_output=True):
    from testing_resources.primes import primes_run_case
    from base.primes import write_primes as base_function
    from sample_solution.primes import write_primes as sample_solution_function
    from student.primes import write_primes as student_function

    project1_results = ProjectResults('Primes', 'Write primes under n to a specified file.')

    project1_results.add_case(primes_run_case(base_function, sample_solution_function, student_function, 1000, '1,000', 'testing_resources/reference_primes_1k.txt'))
    project1_results.add_case(primes_run_case(base_function, sample_solution_function, student_function, 10000, '10,000', 'testing_resources/reference_primes_10k.txt'))

    if print_project_level_output:
        project1_results.print_results()

    return project1_results

def test_uncertain_cuboids(print_project_level_output=True):
    from testing_resources.uncertain_cuboids import uncertain_cuboids_run_case
    from base.uncertain_cuboids import calculate_uncertain_cuboid_statistics as base_function
    from sample_solution.uncertain_cuboids import calculate_uncertain_cuboid_statistics as sample_solution_function
    from student.uncertain_cuboids import calculate_uncertain_cuboid_statistics as student_function

    project1_results = ProjectResults('Uncertain Cuboids', 'Calculate the mean and standard deviation of the volume of cuboids with uncertain dimensions.')

    project1_results.add_case(uncertain_cuboids_run_case(base_function, sample_solution_function, student_function, 1e6, '1,000,000', 10, 5, 3, 0.5, 0.2, 0.1, (149.99, 150.01), (3.11, 3.15)))

    project1_results.add_case(uncertain_cuboids_run_case(base_function, sample_solution_function, student_function, 1e6, '1,000,000', 4, 5, 2, 0, 0, 0, (39.999, 40.001), (0, 0.0001)))

    project1_results.add_case(uncertain_cuboids_run_case(base_function, sample_solution_function, student_function, 1e6, '1,000,000', 3, 10, 2, 1, 0, 0, (59, 61), (5.75, 5.78)))

    if print_project_level_output:
        project1_results.print_results()




if __name__ == '__main__':
    #run_tests()
    test_uncertain_cuboids()