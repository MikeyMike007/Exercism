import string

def is_pangram(sentence):
    alphabet = string.ascii_lowercase

    for char in alphabet:
        if char not in sentence.lower():
            return False

    return True

