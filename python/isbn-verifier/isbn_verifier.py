import string

def is_valid(isbn: str) -> bool:
    """
    Check wether a string is a valid isbn code.
    """
    # Gather the weights in a list. From 10 to 1.
    weights = [weight for weight in range(10, 0, -1)]

    # Extract all digits from the isbn string
    digits = [int(char) for char in isbn[:-1] if char in string.digits]

    # ---------------------------------------------------------
    # Some validity checking and the addition of the last item.
    # ---------------------------------------------------------

    # 1. Check whether the length of the digits list is equal to 9 and the last item in
    # the string isbn is equal to an 'X'. In that case digits is appended with
    # number ten according to the specification.
    if len(digits) == 9 and isbn[-1] == 'X':
        digits.append(10)

    # 2. Check whether the length of the digits list is equal to 9 and the last
    # item in the isbn string is a digit. In that case we add the digit to the
    # end of the list digits.
    elif len(digits) == 9 and isbn[-1] in string.digits:
        digits.append(int(isbn[-1]))

    # 3. In all other cases, the isbn string doesnt represent a correct isbn
    # number.
    else:
        return False

    # Return True if the isbn formula is true
    return sum(digit * weight for digit, weight in zip(digits,weights)) % 11 == 0
