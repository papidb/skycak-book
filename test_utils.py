from typing import List, Dict, Any, Tuple

def run_tests(tests: List[Dict[str, Any]]) -> Tuple[int, int]:
    """
    Run a list of test cases and report results.

    Each test should be a dictionary with:
    - 'function': the function to test
    - 'input': the input value(s) - use tuple for multiple parameters
    - 'output': the expected output

    Returns:
        Tuple of (num_successes, num_failures)
    """
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
    return num_successes, num_failures
