import random


def random_draw(distribution: list[int]) -> int:
    if sum(distribution) != 1:
        return 0
    cumulative_distribution = list(distribution)
    random_number = random.random()

    for i in range(1, len(distribution)):
        cumulative_distribution[i] = cumulative_distribution[i - 1] + distribution[i]
        if random_number < cumulative_distribution[i]:
            return cumulative_distribution[i]
    return 0


if __name__ == "__main__":
    print(random_draw([0.4, 0.2, 0.2, 0.2]))
