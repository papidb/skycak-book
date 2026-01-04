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


def generate_collatz_sequence(n: int) -> list:
    """
    Generate an array containing the first n terms of the Collatz sequence.
    Starting with 25, if previous is even: divide by 2, if odd: multiply by 3 and add 1.
    """
    result = []
    for i in range(n):
        result.append(get_nth_term_collatz(i + 1))
    return result


def get_nth_term_collatz(n: int) -> int:
    """
    Recursively generate the nth term of the Collatz sequence.
    Starting with 25, if previous is even: divide by 2, if odd: multiply by 3 and add 1.
    """
    if n == 1:
        return 25
    previous = get_nth_term_collatz(n - 1)
    if previous % 2 == 0:
        return previous / 2
    return (previous * 3) + 1


def generate_fibonacci_sequence(n: int) -> list:
    """
    Generate an array containing the first n terms of the Fibonacci sequence.
    Starting with 0, 1, each term is the sum of the previous two terms.
    """
    result = []

    for i in range(n):
        result.append(get_nth_term_fibonacci(i + 1))

    return result


def get_nth_term_fibonacci(n: int) -> int:
    """
    Recursively generate the nth term of the Fibonacci sequence.
    Starting with 0, 1, each term is the sum of the previous two terms.
    """
    if n == 1:
        return 0
    if n == 2:
        return 1

    return get_nth_term_fibonacci(n - 2) + get_nth_term_fibonacci(n - 1)


def generate_product_sequence(n: int) -> list:
    """
    Generate an array containing the first n terms of the product sequence.
    Starting with 2, -3, each term is the product of the previous two terms.
    """
    result = []

    for i in range(n):
        result.append(get_nth_term_product(i + 1))

    return result


def get_nth_term_product(n: int) -> int:
    """
    Recursively generate the nth term of the product sequence.
    Starting with 2, -3, each term is the product of the previous two terms.
    """
    if n == 1:
        return 2
    if n == 2:
        return -3

    return get_nth_term_product(n - 2) * get_nth_term_product(n - 1)
