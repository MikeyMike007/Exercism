import string


def is_isogram(sentence: str) -> bool:
    """
    Determine whether a sentence is an isogram.
    """
    # Get rid of all spaces, hyphens and all other characters that are not
    # ascii letters
    sentence = ''.join(char for char in sentence.lower()
                       if char in string.ascii_lowercase)

    for i in range(len(sentence) - 1):
        # Check whether current loop character already has been looped though.
        # In this case, the sentence is not an isogram.
        if sentence[i + 1] in sentence[:i + 1]:
            return False
    return True
