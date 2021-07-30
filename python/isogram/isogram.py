import string


def is_isogram(sentence: str) -> bool:
    """
    Determine whether a sentence is an isogram.
    """
    # Get rid of all spaces, hyphens and all other characters that are not
    # ascii letters
    sentence = ''.join(char for char in sentence.lower()
                       if char in string.ascii_lowercase)

    # Check if the sentence has unique characters. If not return false otherwise
    # return true
    return len(set(sentence)) == len(sentence)
