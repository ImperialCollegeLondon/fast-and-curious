def fibonacci(n, memo=None):
    """
    Calculate the nth Fibonacci number using memoization.

    The Fibonacci sequence is a series of numbers where each number is the sum 
    of the two preceding ones, usually starting with 0 and 1. This function 
    uses a recursive approach with memoization to calculate the Fibonacci number 
    at position n efficiently.

    Parameters:
    n (int): The position in the Fibonacci sequence to calculate. Must be a non-negative integer.
    memo (dict, optional): A dictionary to store previously calculated Fibonacci numbers to 
                           avoid redundant calculations. Defaults to None.

    Returns:
    int: The nth Fibonacci number.

    Examples:
    >>> fibonacci(0)
    0
    >>> fibonacci(1)
    1
    >>> fibonacci(5)
    5
    >>> fibonacci(9)
    34
    """
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]


# n = 35
# print(f"Trying this solution: Fibonacci({n}) = {fibonacci(n)}")
