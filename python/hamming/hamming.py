def distance(strand_a: str, strand_b: str) -> int:
    """
    Calculate and return the hamming distance of two strings.
    """
    # Raise a value-error if strings are not of the same length.
    if len(strand_a) != len(strand_b):
        raise ValueError("Error: Strings not of equal length")

    # Return the number of occurences when the characters of strand_a and
    # strand_b not are the same
    result = sum(1 for a_char, b_char in zip(strand_a, strand_b)
                 if a_char != b_char)
    return result
