# optimised solution
import math
import numpy as np
def largest_triangle_proof(n, radius):
    """
    Prove the pattern of largest area of a triangle that can be 
    inscribed inside a give circle. 
    
    This function returns the height of largest area of a triangle 
    that can be inscribed inside a circle with the given radius, 
    and base of the triangle is the diameter of the circle

    by Dr Liam Gao (RCDS) June 2024 

    Args:
      radius: radius of the circle
      n: gradient

    Returns:
      height of the largest triangle
    """
    
    # set the centre of the circle to (0,0)
    origin_x = 0.0
    origin_y = 0.0

    #The lower this value the higher quality the circle is with more points generated
    stepSize = 180/n
    if stepSize < 1:
        stepSize = 1

    largest_area = 0.0
    t = 0.0
    best_h = 0.0
    base_length = 2 * radius
    while t<=90: # using degrees
        radian_t = math.radians(t)
        h = radius * math.sin(radian_t)
        tmp_area = 0.5 * base_length * h
        if tmp_area > largest_area:
            best_h = h
        largest_area = max(largest_area, tmp_area)
        
        t += stepSize
    
    return(best_h)

def largest_triangle_area(n, radius, h=0.0):
    """
    Returns the largest area of a triangle that can be inscribed inside a
    circle with the given radius.

    Args:
      n: gradient
      radius: radius of the circle
      h: the starting height of triangle found after the proof of max area based on diameter as the base of triangle
      

    Returns:
      Area of the largest inscribed triangle
    """

    h = largest_triangle_proof(n, radius)
    # The largest triangle is an equilateral triangle
    largest_A = 0.0
    step = radius / n
    if step<0.1:
        step = 0.1
    d = 0.0 

    while d < radius:
        base_length = 2 * math.sqrt(radius**2 - d**2)
        area = 0.5 * base_length * (d + h)
        largest_A = max(largest_A, area)
        d += step
    print(f"The largest area of a triangle inscribed in a circle with radius {radius} is {largest_A:.2f} \n ")
    return largest_A

# Example usage
#import time
#radius = 50
#t0 = time.time()
#height = largest_triangle_proof(500, radius)
#max_area = largest_triangle_area(500, radius, height)
#t1 = time.time()
#print(f"The largest area of a triangle inscribed in a circle with radius {radius} is {max_area:.2f} \n Runtime was {t1-t0:.5f}")