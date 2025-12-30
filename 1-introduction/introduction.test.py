from introduction import (
    check_if_symmetric,
    convert_to_numbers,
    convert_to_letters,
    get_intersection,
    get_union,
    count_characters,
    is_prime
)

tests = [
    # check_if_symmetric tests
    {
        'function': check_if_symmetric,
        'input': 'racecar',
        'output': True
    },
    {
        'function': check_if_symmetric,
        'input': 'batman',
        'output': False
    },
    {
        'function': check_if_symmetric,
        'input': 'a',
        'output': True
    },
    {
        'function': check_if_symmetric,
        'input': 'aa',
        'output': True
    },
    {
        'function': check_if_symmetric,
        'input': '',
        'output': False
    },
    {
        'function': check_if_symmetric,
        'input': 'noon',
        'output': True
    },
    {
        'function': check_if_symmetric,
        'input': 'radar',
        'output': True
    },

    # convert_to_numbers tests
    {
        'function': convert_to_numbers,
        'input': 'a cat',
        'output': [1, 0, 3, 1, 20]
    },
    {
        'function': convert_to_numbers,
        'input': 'abc',
        'output': [1, 2, 3]
    },
    {
        'function': convert_to_numbers,
        'input': 'z',
        'output': [26]
    },
    {
        'function': convert_to_numbers,
        'input': ' ',
        'output': [0]
    },

    # convert_to_letters tests
    {
        'function': convert_to_letters,
        'input': [1, 0, 3, 1, 20],
        'output': 'a cat'
    },
    {
        'function': convert_to_letters,
        'input': [1, 2, 3],
        'output': 'abc'
    },
    {
        'function': convert_to_letters,
        'input': [26],
        'output': 'z'
    },
    {
        'function': convert_to_letters,
        'input': [0],
        'output': ' '
    },

    # get_intersection tests
    {
        'function': get_intersection,
        'input': ([1, 2, 4], [3, 1, 9, 2]),
        'output': [1, 2]
    },
    {
        'function': get_intersection,
        'input': ([1, 2, 3], [4, 5, 6]),
        'output': []
    },
    {
        'function': get_intersection,
        'input': ([1, 2, 3], [1, 2, 3]),
        'output': [1, 2, 3]
    },
    {
        'function': get_intersection,
        'input': ([], [1, 2, 3]),
        'output': []
    },
    {
        'function': get_intersection,
        'input': ([5, 5, 5], [5, 5]),
        'output': [5]
    },

    # get_union tests
    {
        'function': get_union,
        'input': ([1, 2, 4], [3, 1, 9, 2]),
        'output': [1, 2, 4, 3, 9]
    },
    {
        'function': get_union,
        'input': ([1, 2, 3], [4, 5, 6]),
        'output': [1, 2, 3, 4, 5, 6]
    },
    {
        'function': get_union,
        'input': ([1, 2, 3], [1, 2, 3]),
        'output': [1, 2, 3]
    },
    {
        'function': get_union,
        'input': ([], [1, 2, 3]),
        'output': [1, 2, 3]
    },
    {
        'function': get_union,
        'input': ([5, 5, 5], [5, 5]),
        'output': [5]
    },

    # count_characters tests
    {
        'function': count_characters,
        'input': 'A cat !!!',
        'output': {'a': 2, ' ': 2, 'c': 1, 't': 1, '!': 3}
    },
    {
        'function': count_characters,
        'input': 'hello',
        'output': {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    },
    {
        'function': count_characters,
        'input': 'aaa',
        'output': {'a': 3}
    },
    {
        'function': count_characters,
        'input': 'AaBbCc',
        'output': {'a': 2, 'b': 2, 'c': 2}
    },
    {
        'function': count_characters,
        'input': '',
        'output': {}
    },

    # is_prime tests
    {
        'function': is_prime,
        'input': 1,
        'output': True
    },
    {
        'function': is_prime,
        'input': 2,
        'output': True
    },
    {
        'function': is_prime,
        'input': 3,
        'output': True
    },
    {
        'function': is_prime,
        'input': 4,
        'output': False
    },
    {
        'function': is_prime,
        'input': 5,
        'output': True
    },
    {
        'function': is_prime,
        'input': 6,
        'output': False
    },
    {
        'function': is_prime,
        'input': 7,
        'output': True
    },
    {
        'function': is_prime,
        'input': 8,
        'output': False
    },
    {
        'function': is_prime,
        'input': 9,
        'output': False
    },
    {
        'function': is_prime,
        'input': 10,
        'output': False
    },
    {
        'function': is_prime,
        'input': 11,
        'output': True
    },
    {
        'function': is_prime,
        'input': 17,
        'output': True
    },
]

num_successes = 0
num_failures = 0

for test in tests:
    function = test['function']
    test_input = test['input']
    desired_output = test['output']

    # Handle functions with multiple parameters
    if isinstance(test_input, tuple):
        actual_output = function(*test_input)
    else:
        actual_output = function(test_input)

    if actual_output == desired_output:
        num_successes += 1
    else:
        num_failures += 1
        function_name = function.__name__
        print('')
        print(f'{function_name} failed on input {test_input}')
        print(f'\tActual output: {actual_output}')
        print(f'\tDesired output: {desired_output}')

print(f'Testing complete: {num_successes} successes and {num_failures} failures.')
