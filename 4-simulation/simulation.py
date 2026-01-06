import random


def sim_probability(num_heads, num_flips, trials=10000):
    # hold container that helps hold the results of the trial
    if num_heads < 0 or num_heads > num_flips:
        return 0.0

    successes = 0

    for _ in range(trials):
        heads = 0
        for _ in range(num_flips):
            if random.random() < 0.5:
                heads += 1
        if heads == num_heads:
            successes += 1

    return successes / trials


def sanity_check(num_flips):
    total = 0.0
    for heads in range(num_flips + 1):
        total += sim_probability(heads, num_flips)
    return total


if __name__ == "__main__":
    print(sim_probability(10, 20))
    print(sanity_check(10))
