import sys
sys.path.append('..')
from test_utils import run_tests

from base import binary_to_decimal

tests = [
    # binary_to_decimal tests
    {
        'function': binary_to_decimal,
        'input': '0',
        'output': 0
    },
    {
        'function': binary_to_decimal,
        'input': '1',
        'output': 1
    },
    {
        'function': binary_to_decimal,
        'input': '10',
        'output': 2
    },
    {
        'function': binary_to_decimal,
        'input': '11',
        'output': 3
    },
    {
        'function': binary_to_decimal,
        'input': '100',
        'output': 4
    },
    {
        'function': binary_to_decimal,
        'input': '101',
        'output': 5
    },
    {
        'function': binary_to_decimal,
        'input': '110',
        'output': 6
    },
    {
        'function': binary_to_decimal,
        'input': '111',
        'output': 7
    },
    {
        'function': binary_to_decimal,
        'input': '1000',
        'output': 8
    },
    {
        'function': binary_to_decimal,
        'input': '1111',
        'output': 15
    },
    {
        'function': binary_to_decimal,
        'input': '10000',
        'output': 16
    },
    {
        'function': binary_to_decimal,
        'input': '11111111',
        'output': 255
    },
    {
        'function': binary_to_decimal,
        'input': '100000000',
        'output': 256
    },
    {
        'function': binary_to_decimal,
        'input': '1010101',
        'output': 85
    },
]

run_tests(tests)
