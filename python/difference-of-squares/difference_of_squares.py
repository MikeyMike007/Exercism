def square_of_sum(number: int) -> int:
    """
    Calculate and return the square of sum for the argument *number*.
    """
    return sum(i for i in range(number + 1))**2


def sum_of_squares(number: int) -> int:
    """
    Calculate and return the sum of squares for the argument *number*.
    """
    return sum(i**2 for i in range(number + 1))


def difference_of_squares(number: int) -> int:
    """
    Calculate and return the difference between square of sum and sum of squares with
    regards to the argument *number*
    """
    return square_of_sum(number) - sum_of_squares(number)
