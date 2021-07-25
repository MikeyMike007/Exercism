def is_armstrong_number(armstrong_candidate: int) -> bool:
    """
    Calculate the number of digits in a number and the armstrong_sum. Return
    true if the armstrong_sum equals the armstrong_candidate
    """

    if armstrong_candidate < 0:
        return False

    nr_digits = nr_digits_number(armstrong_candidate)
    a_sum = armstrong_sum(armstrong_candidate, nr_digits)

    return True if a_sum == armstrong_candidate else False

def nr_digits_number(armstrong_candidate: int) -> int:
    """
    Estimate the number of digits in a number. Return the number of digits.
    """
    number_of_digits = 0
    while armstrong_candidate != 0:
        armstrong_candidate = int(armstrong_candidate / 10)
        number_of_digits += 1

    return number_of_digits

def armstrong_sum(armstrong_candidate: int, nr_digits: int) -> int:
    """
    Calculate and return the armstrong_sum
    """
    a_sum = 0

    while armstrong_candidate != 0:
        digit_in_armstrong_candidate = armstrong_candidate % 10
        a_sum += digit_in_armstrong_candidate ** nr_digits
        armstrong_candidate = int(armstrong_candidate / 10)
    return a_sum

