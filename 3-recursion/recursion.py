def generate_sequence_1(n: int) -> list:
    """
    Generate an array containing the first n terms of the sequence.
    Starting with 5, each term = previous * 3 - 4.
    """
    result = []
    for i in range(n):
        result.append(get_nth_term_sequence_1(i + 1))
    return result


def get_nth_term_sequence_1(n: int) -> int:
    """
    Recursively generate the nth term of the sequence.
    Starting with 5, each term = previous * 3 - 4.
    """
    if n == 1:
        return 5
    return (get_nth_term_sequence_1(n - 1) * 3) - 4
