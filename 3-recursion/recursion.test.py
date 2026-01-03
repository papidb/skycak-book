import sys
sys.path.append('..')
from test_utils import run_tests

from recursion import generate_sequence_1, get_nth_term_sequence_1

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
]

run_tests(tests)
