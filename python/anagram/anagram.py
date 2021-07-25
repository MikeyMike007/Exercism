def find_anagrams(word: str, candidates: list[str]) -> list[str]:
    """
    Return a list of anagrams.
    """
    return [
        candidate for candidate in candidates if is_anagram(word, candidate)
    ]


def is_anagram(word: str, candidate: str) -> bool:
    """
    Determine if the candidate string is an anagram of the word string.
    """
    # Make the strings lowercase
    word = word.lower()
    candidate = candidate.lower()

    # If the length of the word and the candidate is not the same, the candidate
    # cannot be an anagram if word. Same yields if word and candidate is the
    # same string.
    if len(word) != len(candidate) or word == candidate:
        return False

    # Check that the count of each character is the same in both word and
    # candidate. If this is the case, the candidate is an anagram of word.
    for char in candidate:
        if word.count(char) != candidate.count(char):
            return False

    return True
