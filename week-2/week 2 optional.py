import math

def polysum(n, s):    
    """

    :param n: number of sides of the polygon
    :param s: length of each side
    :return: the area of the polygon, plus the square of the perimeter.
    This value must be rounded to 4 decimal places.
    """
    area = (0.25 * n * s**2) / (math.tan(math.pi / n))
    perimeterSquared = (n * s) ** 2
    return round(area + perimeterSquared, 4)
