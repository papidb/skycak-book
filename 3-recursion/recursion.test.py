import sys
sys.path.append('..')
from test_utils import run_tests

from recursion import generate_sequence_1, get_nth_term_sequence_1, generate_collatz_sequence, get_nth_term_collatz

tests = [
    # generate_sequence_1 tests
    {
        'function': generate_sequence_1,
        'input': 1,
        'output': [5]
    },
    {
        'function': generate_sequence_1,
        'input': 2,
        'output': [5, 11]
    },
    {
        'function': generate_sequence_1,
        'input': 3,
        'output': [5, 11, 29]
    },
    {
        'function': generate_sequence_1,
        'input': 4,
        'output': [5, 11, 29, 83]
    },
    {
        'function': generate_sequence_1,
        'input': 5,
        'output': [5, 11, 29, 83, 245]
    },
    {
        'function': generate_sequence_1,
        'input': 6,
        'output': [5, 11, 29, 83, 245, 731]
    },
    {
        'function': generate_sequence_1,
        'input': 7,
        'output': [5, 11, 29, 83, 245, 731, 2189]
    },
    {
        'function': generate_sequence_1,
        'input': 0,
        'output': []
    },

    # get_nth_term_sequence_1 tests
    {
        'function': get_nth_term_sequence_1,
        'input': 1,
        'output': 5
    },
    {
        'function': get_nth_term_sequence_1,
        'input': 2,
        'output': 11
    },
    {
        'function': get_nth_term_sequence_1,
        'input': 3,
        'output': 29
    },
    {
        'function': get_nth_term_sequence_1,
        'input': 4,
        'output': 83
    },
    {
        'function': get_nth_term_sequence_1,
        'input': 5,
        'output': 245
    },
    {
        'function': get_nth_term_sequence_1,
        'input': 6,
        'output': 731
    },
    {
        'function': get_nth_term_sequence_1,
        'input': 7,
        'output': 2189
    },
    {
        'function': get_nth_term_sequence_1,
        'input': 8,
        'output': 6563
    },
    {
        'function': get_nth_term_sequence_1,
        'input': 10,
        'output': 59051
    },

    # generate_collatz_sequence tests
    {
        'function': generate_collatz_sequence,
        'input': 1,
        'output': [25]
    },
    {
        'function': generate_collatz_sequence,
        'input': 2,
        'output': [25, 76]
    },
    {
        'function': generate_collatz_sequence,
        'input': 3,
        'output': [25, 76, 38]
    },
    {
        'function': generate_collatz_sequence,
        'input': 4,
        'output': [25, 76, 38, 19]
    },
    {
        'function': generate_collatz_sequence,
        'input': 5,
        'output': [25, 76, 38, 19, 58]
    },
    {
        'function': generate_collatz_sequence,
        'input': 6,
        'output': [25, 76, 38, 19, 58, 29]
    },
    {
        'function': generate_collatz_sequence,
        'input': 7,
        'output': [25, 76, 38, 19, 58, 29, 88]
    },
    {
        'function': generate_collatz_sequence,
        'input': 10,
        'output': [25, 76, 38, 19, 58, 29, 88, 44, 22, 11]
    },
    {
        'function': generate_collatz_sequence,
        'input': 0,
        'output': []
    },

    # get_nth_term_collatz tests
    {
        'function': get_nth_term_collatz,
        'input': 1,
        'output': 25
    },
    {
        'function': get_nth_term_collatz,
        'input': 2,
        'output': 76
    },
    {
        'function': get_nth_term_collatz,
        'input': 3,
        'output': 38
    },
    {
        'function': get_nth_term_collatz,
        'input': 4,
        'output': 19
    },
    {
        'function': get_nth_term_collatz,
        'input': 5,
        'output': 58
    },
    {
        'function': get_nth_term_collatz,
        'input': 6,
        'output': 29
    },
    {
        'function': get_nth_term_collatz,
        'input': 7,
        'output': 88
    },
    {
        'function': get_nth_term_collatz,
        'input': 8,
        'output': 44
    },
    {
        'function': get_nth_term_collatz,
        'input': 9,
        'output': 22
    },
    {
        'function': get_nth_term_collatz,
        'input': 10,
        'output': 11
    },
    {
        'function': get_nth_term_collatz,
        'input': 11,
        'output': 34
    },
    {
        'function': get_nth_term_collatz,
        'input': 12,
        'output': 17
    },
]

run_tests(tests)
