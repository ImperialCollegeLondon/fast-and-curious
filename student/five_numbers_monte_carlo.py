# sample solution

import random, statistics, time


"""
  Generates all possible five random numbers satisfying:
      - Median: 7
      - Mode: 8 only (appears most frequently)
      - Range: 5 (difference between largest and smallest number)
"""


def mode(lst):
    """
    Find the Mode(s) of the given list.
      
    Args:
        lst: a list

    Returns:
        Mode(s) in a list.
    """
    if lst==[]:
        return None
    else:
        return statistics.multimode(lst)
            
def generate_numbers(n, median, mode_, range_):
    """
    Generates all possible five random numbers satisfying the given:
      - Median:
      - Mode: 
      - Range:
      
    Args:
      n: repeat n time to find all answers.
      median: Target median value.
      mode_: Target mode value (most frequent number).
      range_: Target range of the numbers.

    Returns:
      A list of five random numbers.
    """
    exp_numbers = False
    while (not exp_numbers):
        numbers = [mode_] * 2  # Two numbers set to the mode
        numbers.append(median)
        min_num = mode_ - range_
        numbers.extend([random.randint(min_num, median) for _ in range(2)])
        # Shuffle the list to randomize positions
        random.shuffle(numbers)
        # check if the range is the same
        range_tmp = max(numbers) - min(numbers)
        if (range_tmp == range_ and len(mode(numbers))==1):
            exp_numbers = True
    
    return numbers

'''Description from testing_interface.ipynb
The file `student/five_numbers_monte_carlo.py contains` two funtions, one checks the mode of a list and the other generates a list consisting of five numbers that satisfy the given range, mode and median. The main function, which is called `generate_numbers`, generates a list consisting of five numbers by constraining the numbers with the given range, median and mode. Several lists are expected to be obtained. This is also an example of a Monte Carlo simulation. 

The function, `generate_numbers`, takes sever arguments:
- `n` is the number of repetition.
- `median`: Target median value.
- `mode_`: Target mode value (most frequent number).
- `range_`: Target range of the numbers.

You need to modify the code appropriately in order to apply a simple Monte Carlo simulation approach to find all five numbers.'''