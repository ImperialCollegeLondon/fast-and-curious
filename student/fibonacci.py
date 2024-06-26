def fibonacci(n):
    """
    Calculate the nth Fibonacci number recursively.

    The Fibonacci sequence is a series of numbers where each number is the sum 
    of the two preceding ones, usually starting with 0 and 1. This function 
    uses a recursive approach to calculate the Fibonacci number at position n.

    Parameters:
    n (int): The position in the Fibonacci sequence to calculate. Must be a non-negative integer.

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
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)



# n = 35
# print(f"Trying this solution: Fibonacci({n}) = {fibonacci(n)}")
