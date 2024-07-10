from testing_resources.common_resources import ProjectResults, print_minor_division, format_number


def run_tests():
    """
    Runs the test cases for each project and prints the results.

    return: None
    """

    # Run the test cases for each project
    project_results = []
    # Add the results of each project to the project_results list
    # Suppress the project level output for each project
    project_results.append(test_primes(print_project_level_output=False))
    project_results.append(test_uncertain_cuboids(print_project_level_output=False))

    project_results.append(test_five_numbers(print_project_level_output=False))
    project_results.append(test_largest_triangle(print_project_level_output=False))

    project_results.append(test_fibonacci(print_project_level_output=False))
    project_results.append(test_shuffling_cards(print_project_level_output=False))

    project_results.append(test_projectiles(print_project_level_output=False))

    # Calculate the total points for all projects
    total_points = sum([project.points for project in project_results])

    # Print the score for each project
    for project in project_results:
        print(f'{project.project_name}: {format_number(project.points)} points')
        print_minor_division()
    # Print the total points
    print(f'Total Points: {format_number(total_points)}')


def test_primes(print_project_level_output=True):
    '''Tests the Primes project.
    :param print_project_level_output: bool, If True, the results of the project will be printed to the console.
    :return: ProjectResults, The results of the project.
    '''
    from testing_resources.primes import primes_run_case
    from base.primes import write_primes as base_function
    from sample_solution.primes import write_primes as sample_solution_function
    from student.primes import write_primes as student_function

    # Create a ProjectResults object to store the results of the project
    project_results = ProjectResults('Primes', 'Write primes under n to a specified file.')

    # Add test cases to the project
    project_results.add_case(primes_run_case(base_function, sample_solution_function, student_function, 1000, '1,000', 'testing_resources/reference_primes_1k.txt'))
    project_results.add_case(primes_run_case(base_function, sample_solution_function, student_function, 10000, '10,000', 'testing_resources/reference_primes_10k.txt'))

    # Print the results of the project if print_project_level_output is True
    if print_project_level_output:
        project_results.print_results()

    # Return the results of the project
    return project_results

def test_fibonacci(print_project_level_output=True):
    '''Tests the Fibonacci project.
    :param print_project_level_output: bool, If True, the results of the project will be printed to the console.
    :return: ProjectResults, The results of the project.
    '''
    from testing_resources.fibonacci import fibonacci_run_case
    from base.fibonacci import fibonacci as base_function
    from sample_solution.fibonacci import fibonacci as sample_solution_function
    from student.fibonacci import fibonacci as student_function

    # Create a ProjectResults object to store the results of the project
    project_results = ProjectResults('Fibonacci', 'Determine the nth fibonacci number.')

    # Add test cases to the project
    project_results.add_case(fibonacci_run_case(base_function, sample_solution_function, student_function, 1))
    project_results.add_case(fibonacci_run_case(base_function, sample_solution_function, student_function, 10))
    project_results.add_case(fibonacci_run_case(base_function, sample_solution_function, student_function, 35))

    # Print the results of the project if print_project_level_output is True
    if print_project_level_output:
        project_results.print_results()

    # Return the results of the project
    return project_results

def test_shuffling_cards(print_project_level_output=True):
    '''Tests the Shuffling Cards project.
    :param print_project_level_output: bool, If True, the results of the project will be printed to the console.
    :return: ProjectResults, The results of the project.
    '''
    from testing_resources.shuffling_cards import shuffling_cards_run_case
    from testing_resources.shuffling_cards_input import case_1_input, case_2_input
    from base.shuffling_cards import find_card_position as base_function
    from sample_solution.shuffling_cards import find_card_position as sample_solution_function
    from student.shuffling_cards import find_card_position as student_function
    

    # Create a ProjectResults object to store the results of the project
    project_results = ProjectResults('Shuffling Cards', 'Determine the card position.')

    # Test case 1
    project_results.add_case(
        shuffling_cards_run_case(base_function, sample_solution_function, student_function, **case_1_input)
    )
    
    # Test case 2
    project_results.add_case(
        shuffling_cards_run_case(base_function, sample_solution_function, student_function, **case_2_input)
    )

    # Print the results of the project if print_project_level_output is True
    if print_project_level_output:
        project_results.print_results()

    # Return the results of the project
    return project_results

def test_uncertain_cuboids(print_project_level_output=True):
    '''Tests the Uncertain Cuboids project.
    :param print_project_level_output: bool, If True, the results of the project will be printed to the console.
    :return: ProjectResults, The results of the project.
    '''

    from testing_resources.uncertain_cuboids import uncertain_cuboids_run_case
    from base.uncertain_cuboids import calculate_uncertain_cuboid_statistics as base_function
    from sample_solution.uncertain_cuboids import calculate_uncertain_cuboid_statistics as sample_solution_function
    from student.uncertain_cuboids import calculate_uncertain_cuboid_statistics as student_function

    # Create a ProjectResults object to store the results of the project
    project_results = ProjectResults('Uncertain Cuboids', 'Calculate the mean and standard deviation of the volume of cuboids with uncertain dimensions.')

    # Add test cases to the project
    project_results.add_case(uncertain_cuboids_run_case(base_function, sample_solution_function, student_function, 1000000, '1,000,000', 10, 5, 3, 0.5, 0.2, 0.1, (149.99, 150.01), (3.11, 3.15)))
    project_results.add_case(uncertain_cuboids_run_case(base_function, sample_solution_function, student_function, 1000000, '1,000,000', 4, 5, 2, 0, 0, 0, (39.999, 40.001), (0, 0.0001)))
    project_results.add_case(uncertain_cuboids_run_case(base_function, sample_solution_function, student_function, 1000000, '1,000,000', 3, 10, 2, 1, 0, 0, (59, 61), (5.75, 5.78)))

    # Print the results of the project if print_project_level_output is True
    if print_project_level_output:
        project_results.print_results()

    # Return the results of the project
    return project_results

def test_five_numbers(print_project_level_output=True):
    '''Tests the five numbers generation.
    :param print_project_level_output: bool, If True, the results of the project will be printed to the console.
    :return: ProjectResults, The results of the project.
    '''
    from testing_resources.five_numbers import  five_numbers_run_case
    from base.five_numbers_monte_carlo import generate_numbers as base_function
    from sample_solution.five_numbers_monte_carlo import generate_numbers as sample_solution_function
    from student.five_numbers_monte_carlo import generate_numbers as student_function

    # Create a ProjectResults object to store the results of the project
    project_results = ProjectResults('Five numbers', 'Generate all five numbers satisfying median of 7, mode of 8 and range of 5')

    # Add test cases to the project
    project_results.add_case(five_numbers_run_case(base_function, sample_solution_function, student_function, 100, median=7, mode_=8, range_=5))

    # Print the results of the project if print_project_level_output is True
    if print_project_level_output:
        project_results.print_results()

    # Return the results of the project
    return project_results

def test_largest_triangle(print_project_level_output=True):
    '''Tests the largest inscribed triangle in a circle.
    :param print_project_level_output: bool, If True, the results of the project will be printed to the console.
    :return: ProjectResults, The results of the project.
    '''
    from testing_resources.largest_triangle import  largest_triangle_run_case
    from base.largest_inscribed_triangle import largest_triangle_area as base_function
    from sample_solution.largest_inscribed_triangle import largest_triangle_area as sample_solution_function
    from student.largest_inscribed_triangle import largest_triangle_area as student_function

    # Create a ProjectResults object to store the results of the project
    project_results = ProjectResults('Largest Inscribed Triangle', 'The largest inscribed triangle in the given circle with radius 50')

    # Add test cases to the project
    project_results.add_case(largest_triangle_run_case(base_function, sample_solution_function, student_function, 500, radius=50, h=0.0))

    # Print the results of the project if print_project_level_output is True
    if print_project_level_output:
        project_results.print_results()

    # Return the results of the project
    return project_results

def test_projectiles(print_project_level_output=True):
    '''Tests the Projectiles project.
    :param print_project_level_output: bool, If True, the results of the project will be printed to the console.
    :return: ProjectResults, The results of the project.
    '''
    from testing_resources.projectiles import projectiles_run_case
    from base.projectiles import find_launch_angle as base_function
    from sample_solution.projectiles import find_launch_angle as sample_solution_function
    from student.projectiles import find_launch_angle as student_function

    # Create a ProjectResults object to store the results of the project
    project_results = ProjectResults('Projectiles', 'Calculate the launch angle of a projectile to hit a target at a given distance.')

    # Add test cases to the project
    project_results.add_case(projectiles_run_case(base_function, sample_solution_function, student_function, 100, 100, 60, 0.5, 0.01, 1.67))
    project_results.add_case(projectiles_run_case(base_function, sample_solution_function, student_function, 0.1, 100, 60, 0.5, 0.01, 10.1))
    project_results.add_case(projectiles_run_case(base_function, sample_solution_function, student_function, 10, 100, 900, 0.5, 0.001, 32.3))

    # Print the results of the project if print_project_level_output is True
    if print_project_level_output:
        project_results.print_results()

    # Return the results of the project
    return project_results

# Run the tests if the file is run directly
if __name__ == '__main__':
    run_tests()

