# student solution
import math
import numpy as np
def largest_triangle_proof(n, radius):
    """
    Prove the pattern of largest area of a triangle that can be 
    inscribed inside a give circle. 
    
    This function returns the height of largest area of a triangle 
    that can be inscribed inside a circle with the given radius, 
    and base of the triangle is the diameter of the circle

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

    #Generated vertices
    positions = []

    triangle_area = []

    t = 0.0
    base_length = 2 * radius
    # while t <= 0.5 * math.pi: #using radian
    while t<=180: # using degrees
        radian_t = math.radians(t)
        h = radius * math.sin(radian_t)
        tmp_area = 0.5 * base_length * h
        if len(triangle_area) == 0:
            triangle_area.append(tmp_area)
            positions.append((radius * math.cos(radian_t) + origin_x, radius * math.sin(radian_t) + origin_y))
        elif tmp_area > max(triangle_area):
            positions.append((radius * math.cos(radian_t) + origin_x, radius * math.sin(radian_t) + origin_y))
            triangle_area.append(tmp_area)
        t += stepSize
    
    largest_area_idx = triangle_area.index(max(triangle_area))

    return(positions[largest_area_idx][1])

def largest_triangle_area(n, radius, h=0.0):
    """
    Returns the largest area of a triangle that can be inscribed inside a
    circle with the given radius.

    Args:
      radius: radius of the circle
      h: the starting height of triangle found after the proof of max area based on diameter as the base of triangle
      n: gradient

    Returns:
      Area of the largest inscribed triangle
    """
    h = largest_triangle_proof(n, radius)
    # The largest triangle is an equilateral triangle
    largest_A = []
    step = radius / n
    
    for d in np.arange(0, radius, step):
        base_length = 2 * math.sqrt(radius**2 - d**2)
        area = 0.5 * base_length * (d + h)
        if len(largest_A) == 0:
            largest_A.append(area)
        elif area>=max(largest_A):
            largest_A.append(area)
    print(f"The largest area of a triangle inscribed in a circle with radius {radius} is {max(largest_A):.2f} \n ")
    return max(largest_A)

# Example usage
# import time
#radius = 50
#t0 = time.time()
#height = largest_triangle_proof(500, radius)
#max_area = largest_triangle_area(500, radius, height)
#t1 = time.time()
#print(f"The largest area of a triangle inscribed in a circle with radius {radius} is {max_area:.2f} \n Runtime was {t1-t0:.5f}")