import math

def quadratic(a, b, c):
    """
    Calculate the roots of a quadratic equation.

    Args:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.

    Returns:
        tuple or float or None: The roots of the quadratic equation. If the determinant is negative, returns None. If the determinant is zero, returns a single root. Otherwise, returns a tuple of two roots.
    """
    determinant = b**2 - 4*a*c
    if determinant < 0:
        return None
    if determinant == 0:
        return -b / (2*a)
    return (-b + math.sqrt(determinant)) / (2*a), (-b - math.sqrt(determinant)) / (2*a)