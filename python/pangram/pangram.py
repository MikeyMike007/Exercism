import string

def is_pangram(sentence: str) -> bool:

    sentence = sentence.lower()

    for char in string.ascii_lowercase:
        if char not in sentence:
            return False

    return True

