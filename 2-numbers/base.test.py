import sys
sys.path.append('..')
from test_utils import run_tests

from base import binary_to_decimal, hexadecimal_to_decimal

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

    # hexadecimal_to_decimal tests
    {
        'function': hexadecimal_to_decimal,
        'input': '0',
        'output': 0
    },
    {
        'function': hexadecimal_to_decimal,
        'input': '1',
        'output': 1
    },
    {
        'function': hexadecimal_to_decimal,
        'input': '9',
        'output': 9
    },
    {
        'function': hexadecimal_to_decimal,
        'input': 'A',
        'output': 10
    },
    {
        'function': hexadecimal_to_decimal,
        'input': 'a',
        'output': 10
    },
    {
        'function': hexadecimal_to_decimal,
        'input': 'F',
        'output': 15
    },
    {
        'function': hexadecimal_to_decimal,
        'input': 'f',
        'output': 15
    },
    {
        'function': hexadecimal_to_decimal,
        'input': '10',
        'output': 16
    },
    {
        'function': hexadecimal_to_decimal,
        'input': '1A',
        'output': 26
    },
    {
        'function': hexadecimal_to_decimal,
        'input': '1a',
        'output': 26
    },
    {
        'function': hexadecimal_to_decimal,
        'input': 'FF',
        'output': 255
    },
    {
        'function': hexadecimal_to_decimal,
        'input': 'ff',
        'output': 255
    },
    {
        'function': hexadecimal_to_decimal,
        'input': '100',
        'output': 256
    },
    {
        'function': hexadecimal_to_decimal,
        'input': 'ABC',
        'output': 2748
    },
    {
        'function': hexadecimal_to_decimal,
        'input': 'abc',
        'output': 2748
    },
    {
        'function': hexadecimal_to_decimal,
        'input': '1000',
        'output': 4096
    },
    {
        'function': hexadecimal_to_decimal,
        'input': 'CAFE',
        'output': 51966
    },
    {
        'function': hexadecimal_to_decimal,
        'input': 'DEAD',
        'output': 57005
    },
    {
        'function': hexadecimal_to_decimal,
        'input': 'BEEF',
        'output': 48879
    },
]

run_tests(tests)
