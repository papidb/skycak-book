import sys
sys.path.append('..')
from test_utils import run_tests

from base import binary_to_decimal, hexadecimal_to_decimal, decimal_to_binary, decimal_to_hexadecimal, binary_to_hexadecimal

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

    # decimal_to_binary tests
    {
        'function': decimal_to_binary,
        'input': 0,
        'output': '0'
    },
    {
        'function': decimal_to_binary,
        'input': 1,
        'output': '1'
    },
    {
        'function': decimal_to_binary,
        'input': 2,
        'output': '10'
    },
    {
        'function': decimal_to_binary,
        'input': 3,
        'output': '11'
    },
    {
        'function': decimal_to_binary,
        'input': 4,
        'output': '100'
    },
    {
        'function': decimal_to_binary,
        'input': 5,
        'output': '101'
    },
    {
        'function': decimal_to_binary,
        'input': 6,
        'output': '110'
    },
    {
        'function': decimal_to_binary,
        'input': 7,
        'output': '111'
    },
    {
        'function': decimal_to_binary,
        'input': 8,
        'output': '1000'
    },
    {
        'function': decimal_to_binary,
        'input': 15,
        'output': '1111'
    },
    {
        'function': decimal_to_binary,
        'input': 16,
        'output': '10000'
    },
    {
        'function': decimal_to_binary,
        'input': 85,
        'output': '1010101'
    },
    {
        'function': decimal_to_binary,
        'input': 255,
        'output': '11111111'
    },
    {
        'function': decimal_to_binary,
        'input': 256,
        'output': '100000000'
    },

    # decimal_to_hexadecimal tests
    {
        'function': decimal_to_hexadecimal,
        'input': 0,
        'output': '0'
    },
    {
        'function': decimal_to_hexadecimal,
        'input': 1,
        'output': '1'
    },
    {
        'function': decimal_to_hexadecimal,
        'input': 9,
        'output': '9'
    },
    {
        'function': decimal_to_hexadecimal,
        'input': 10,
        'output': 'A'
    },
    {
        'function': decimal_to_hexadecimal,
        'input': 15,
        'output': 'F'
    },
    {
        'function': decimal_to_hexadecimal,
        'input': 16,
        'output': '10'
    },
    {
        'function': decimal_to_hexadecimal,
        'input': 26,
        'output': '1A'
    },
    {
        'function': decimal_to_hexadecimal,
        'input': 255,
        'output': 'FF'
    },
    {
        'function': decimal_to_hexadecimal,
        'input': 256,
        'output': '100'
    },
    {
        'function': decimal_to_hexadecimal,
        'input': 2748,
        'output': 'ABC'
    },
    {
        'function': decimal_to_hexadecimal,
        'input': 4096,
        'output': '1000'
    },
    {
        'function': decimal_to_hexadecimal,
        'input': 51966,
        'output': 'CAFE'
    },
    {
        'function': decimal_to_hexadecimal,
        'input': 57005,
        'output': 'DEAD'
    },
    {
        'function': decimal_to_hexadecimal,
        'input': 48879,
        'output': 'BEEF'
    },

    # binary_to_hexadecimal tests
    {
        'function': binary_to_hexadecimal,
        'input': '0',
        'output': '0'
    },
    {
        'function': binary_to_hexadecimal,
        'input': '1',
        'output': '1'
    },
    {
        'function': binary_to_hexadecimal,
        'input': '1001',
        'output': '9'
    },
    {
        'function': binary_to_hexadecimal,
        'input': '1010',
        'output': 'A'
    },
    {
        'function': binary_to_hexadecimal,
        'input': '1111',
        'output': 'F'
    },
    {
        'function': binary_to_hexadecimal,
        'input': '10000',
        'output': '10'
    },
    {
        'function': binary_to_hexadecimal,
        'input': '11010',
        'output': '1A'
    },
    {
        'function': binary_to_hexadecimal,
        'input': '11111111',
        'output': 'FF'
    },
    {
        'function': binary_to_hexadecimal,
        'input': '100000000',
        'output': '100'
    },
    {
        'function': binary_to_hexadecimal,
        'input': '101010111100',
        'output': 'ABC'
    },
    {
        'function': binary_to_hexadecimal,
        'input': '1000000000000',
        'output': '1000'
    },
    {
        'function': binary_to_hexadecimal,
        'input': '1100101011111110',
        'output': 'CAFE'
    },
    {
        'function': binary_to_hexadecimal,
        'input': '1101111010101101',
        'output': 'DEAD'
    },
    {
        'function': binary_to_hexadecimal,
        'input': '1011111011101111',
        'output': 'BEEF'
    },
]

run_tests(tests)
