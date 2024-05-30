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
            
def generate_numbers(median, mode_, range_):
    """
    Generates all possible five random numbers satisfying the given:
      - Median:
      - Mode: 
      - Range:
      
    Args:
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

# generate lists using Monte Carlo method
"""
list_numbers = []
for i in range(1000):
    numbers = generate_numbers(median=7, mode_=8, range_=5)
    found = False
    for lst in list_numbers:
        tmp_found = False
        if len(list(set(lst)-set(numbers))) == 0:
            tmp_found = True
        found = found or tmp_found
    if not found:
        list_numbers.append(numbers)
print(list_numbers)

"""
