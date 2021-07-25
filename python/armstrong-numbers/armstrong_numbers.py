def is_armstrong_number(armstrong_candidate: int) -> bool:

    if armstrong_candidate < 0:
        return False

    armstrong_candidate_s = str(armstrong_candidate)
    armstrong_sum = 0

    for digit_s in armstrong_candidate_s:
        armstrong_sum += int(digit_s) ** len(armstrong_candidate_s)

    return True if armstrong_sum == armstrong_candidate else False

