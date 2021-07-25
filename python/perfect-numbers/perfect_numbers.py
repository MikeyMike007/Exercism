def classify(number: int) -> str:
    """
    Calculate factors and aliquot sum of a number. Return numbers category.
    """
    if (number <= 0):
        raise ValueError("number cannot be smaller or equal to zero")

    factors = factorify(number)
    aliquot_sum = aliquot(factors)

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"

    

def factorify(number: int) -> list:
    """
    Calculate factors of a number. Return factors in a list.
    """
    factors = []
    for is_factor in range(1,number):
        if number % is_factor == 0:
            factors.append(is_factor)

    return factors

def aliquot(factors: list) -> int:
    """
    Calculate and return aliquot sum
    """
    return sum(factors)
