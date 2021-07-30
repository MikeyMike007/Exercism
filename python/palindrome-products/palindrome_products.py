def largest(min_factor, max_factor):
    """
    Determine and return:
    
        1. Largest palindrome product for two numbers between min_factor and
        max_factor.
        2. The factors relating to the largest palindrom product i.e. if i * j
        is the largest palindrome between min_factor and max_factor. A list of
        [i, j] will be returned together with the palindrom product.
    """

    # Error checking
    if (max_factor < min_factor):
        raise ValueError("Error")

    # Check if max_factor == min_factor
    if (max_factor == min_factor):
        return None, []

    # Store all numbers between min_factor and max_product in a list
    range_numbers = [number for number in range(min_factor, max_factor + 1)]

    # Extract pairs of two numbers between min_factor and max_factor -
    # skip any duplicates i.e. only (i,j) is used for the pairs (i, j) and
    # (j, i)
    factor_candidates = combinations(range_numbers)

    # Save all the products and factors for all palindromes
    products_and_factors = [[i * j, [i, j]] for i, j in factor_candidates
                            if is_palindrome(i * j)]

    # Check whether there are no palindromes.
    if len(products_and_factors) == 0:
        return None, []

    # Determine the max product
    max = max_product(products_and_factors)

    # Save all the factors that has the same product as max
    max_factors = [
        factors for value, factors in products_and_factors if value == max
    ]

    # Return max and its factors
    return max, max_factors


def smallest(min_factor, max_factor):
    """
    Determine and return:
        
    1. Smallest palindrome product for two numbers between min_factor and
    max_factor.
    
    2. The factors relating to the smallest palindrom product i.e. if i * j
            is the largest palindrome between min_factor and max_factor. A list of
            [i, j] will be returned together with the palindrom product.
    """
    # ----------------------------------------------------------------------------
    #
    # Please note that the following code is almost identical as the function
    # largest() except that this function returns the smallest palindrome product
    # and its factors in the set. For comments, please see the function largest() above.
    #
    # ----------------------------------------------------------------------------

    if (max_factor < min_factor):
        raise ValueError("Error")

    if (max_factor == min_factor):
        return None, []

    range_numbers = [number for number in range(min_factor, max_factor + 1)]
    factor_candidates = combinations(range_numbers)

    products_and_factors = [[i * j, [i, j]] for i, j in factor_candidates
                            if is_palindrome(i * j)]

    if len(products_and_factors) == 0:
        return None, []

    min = min_product(products_and_factors)

    min_factors = [
        factors for value, factors in products_and_factors if value == min
    ]

    return min, min_factors


def max_product(products_and_factors):
    """
    Return the largest product in a list.
    """
    return max([product[0] for product in products_and_factors])


def min_product(products_and_factors):
    """
    Return the smallest product in a list.
    """
    return min([product[0] for product in products_and_factors])


def is_palindrome(nr: int) -> bool:
    """
    Check if a number is a palindrome.
    """
    return str(nr) == str(nr)[::-1]


def combinations(numbers: list[int]) -> set:
    """
    Determine all number pairs in the list numbers.
    """
    numbers_set = set()

    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
            numbers_set.add((numbers[i], numbers[j]))

    return numbers_set
