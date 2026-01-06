import sys

sys.path.append("..")
from test_utils import run_tests
from simulation import sim_probability, sanity_check

# Deterministic edge case tests
tests = [
    # Test invalid inputs (negative num_heads)
    {
        'function': sim_probability,
        'input': (-1, 10),
        'output': 0.0
    },
    # Test invalid inputs (num_heads > num_flips)
    {
        'function': sim_probability,
        'input': (11, 10),
        'output': 0.0
    },
    {
        'function': sim_probability,
        'input': (5, 3),
        'output': 0.0
    },
    # Test invalid inputs (negative num_heads with custom trials)
    {
        'function': sim_probability,
        'input': (-5, 10, 1000),
        'output': 0.0
    },
]

print("Running deterministic edge case tests...")
num_successes, num_failures = run_tests(tests)

# Probabilistic tests - these check for reasonable ranges
print("\nRunning probabilistic tests...")

def test_in_range(actual, expected, tolerance, test_name):
    """Helper to test if actual is within tolerance of expected"""
    if abs(actual - expected) <= tolerance:
        return True, None
    else:
        return False, f"{test_name} failed: expected ~{expected} (±{tolerance}), got {actual}"

probabilistic_tests = [
    # All heads in 3 flips should be ~0.125 (1/8)
    (sim_probability(3, 3, trials=10000), 0.125, 0.025, "All heads (3 flips)"),

    # All tails in 3 flips should be ~0.125 (1/8)
    (sim_probability(0, 3, trials=10000), 0.125, 0.025, "All tails (3 flips)"),

    # Exactly 2 heads in 4 flips should be ~0.375 (6/16)
    (sim_probability(2, 4, trials=10000), 0.375, 0.035, "Exactly 2 heads in 4 flips"),

    # Single flip single head should be ~0.5
    (sim_probability(1, 1, trials=10000), 0.5, 0.035, "Single flip single head"),

    # Single flip zero heads should be ~0.5
    (sim_probability(0, 1, trials=10000), 0.5, 0.035, "Single flip zero heads"),

    # 5 heads in 10 flips should be most likely (~0.246)
    (sim_probability(5, 10, trials=10000), 0.246, 0.03, "5 heads in 10 flips"),

    # Zero heads in 0 flips should be 1.0 (certain event)
    (sim_probability(0, 0, trials=1000), 1.0, 0.1, "Zero heads in zero flips"),
]

prob_successes = 0
prob_failures = 0

for actual, expected, tolerance, test_name in probabilistic_tests:
    success, error_msg = test_in_range(actual, expected, tolerance, test_name)
    if success:
        prob_successes += 1
    else:
        prob_failures += 1
        print(f"\n{error_msg}")

# Test that probabilities are always in valid range [0, 1]
print("\nTesting probability range constraints...")
range_tests_passed = 0
range_tests_failed = 0

for heads in range(6):
    result = sim_probability(heads, 5, trials=1000)
    if 0.0 <= result <= 1.0:
        range_tests_passed += 1
    else:
        range_tests_failed += 1
        print(f"\nRange test failed: sim_probability({heads}, 5) = {result} (outside [0, 1])")

# Test that middle values have higher probability than extremes
print("\nTesting probability distribution shape...")
result_middle = sim_probability(5, 10, trials=10000)
result_low = sim_probability(0, 10, trials=10000)
result_high = sim_probability(10, 10, trials=10000)

distribution_tests_passed = 0
distribution_tests_failed = 0

if result_middle > result_low:
    distribution_tests_passed += 1
else:
    distribution_tests_failed += 1
    print(f"\nDistribution test failed: P(5|10) = {result_middle} should be > P(0|10) = {result_low}")

if result_middle > result_high:
    distribution_tests_passed += 1
else:
    distribution_tests_failed += 1
    print(f"\nDistribution test failed: P(5|10) = {result_middle} should be > P(10|10) = {result_high}")

# Sanity check tests - probabilities should sum to ~1.0
print("\nTesting sanity_check function...")
sanity_tests = [
    (sanity_check(1), 1.0, 0.05, "sanity_check(1)"),
    (sanity_check(5), 1.0, 0.05, "sanity_check(5)"),
    (sanity_check(10), 1.0, 0.06, "sanity_check(10)"),
    (sanity_check(0), 1.0, 0.05, "sanity_check(0)"),
]

sanity_successes = 0
sanity_failures = 0

for actual, expected, tolerance, test_name in sanity_tests:
    success, error_msg = test_in_range(actual, expected, tolerance, test_name)
    if success:
        sanity_successes += 1
    else:
        sanity_failures += 1
        print(f"\n{error_msg}")

# Print summary
print("\n" + "="*60)
print("TEST SUMMARY")
print("="*60)
print(f"Deterministic tests: {num_successes} passed, {num_failures} failed")
print(f"Probabilistic tests: {prob_successes} passed, {prob_failures} failed")
print(f"Range tests: {range_tests_passed} passed, {range_tests_failed} failed")
print(f"Distribution tests: {distribution_tests_passed} passed, {distribution_tests_failed} failed")
print(f"Sanity check tests: {sanity_successes} passed, {sanity_failures} failed")

total_passed = num_successes + prob_successes + range_tests_passed + distribution_tests_passed + sanity_successes
total_failed = num_failures + prob_failures + range_tests_failed + distribution_tests_failed + sanity_failures

print(f"\nTotal: {total_passed} passed, {total_failed} failed")
print("="*60)
