def is_triangle(a, b, c):
    """
    Check if three lengths can form a triangle.

    :param a: Length of the first side
    :param b: Length of the second side
    :param c: Length of the third side
    :return: True if they can form a triangle, False otherwise
    """
    return a + b > c and a + c > b and b + c > a

if __name__ == "__main__":
    # Example usage
    print(is_triangle(3, 4, 5))  # True
    print(is_triangle(1, 2, 3))  # False
    print(is_triangle(5, 5, 5))  # True
    print(is_triangle(10, 1, 1))  # False
    print(is_triangle(7, 10, 5))  # True