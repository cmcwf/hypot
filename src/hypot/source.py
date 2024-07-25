# Requirement

# 2 inputs, positive, integer or float (is digit)
# 1 output, float
# external library? No external library
# Create a function - calculate hypot = sqrt(a^2+b^2)
# Create square root function: positive -> float


def hypot(a: int | float, b: int | float) -> float:
    """Calculate a hypotenuse from the length of the two other sides of the triangle

    Args:
        a (int, float): First side of the triangle
        b (int, float): Second side of the triangle

    Returns:
        float: hypotenuse
    """
    return sqrt(a**2 + b**2)


def sqrt(c: int | float) -> float:
    """Calculate square root of a number

    Args:
        c (int, float): positive number only
    Returns:
        float: square root value
    """
    return c**0.5


print(hypot(int(input("a?")), int(input("b?"))))
