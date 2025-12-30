import math

word_number_map = {
    " ": 0,
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
    "i": 9,
    "j": 10,
    "k": 11,
    "l": 12,
    "m": 13,
    "n": 14,
    "o": 15,
    "p": 16,
    "q": 17,
    "r": 18,
    "s": 19,
    "t": 20,
    "u": 21,
    "v": 22,
    "w": 23,
    "x": 24,
    "y": 25,
    "z": 26,
}

number_word_map = {
    0: " ",
    1: "a",
    2: "b",
    3: "c",
    4: "d",
    5: "e",
    6: "f",
    7: "g",
    8: "h",
    9: "i",
    10: "j",
    11: "k",
    12: "l",
    13: "m",
    14: "n",
    15: "o",
    16: "p",
    17: "q",
    18: "r",
    19: "s",
    20: "t",
    21: "u",
    22: "v",
    23: "w",
    24: "x",
    25: "y",
    26: "z",
}


def main():
    print("Hello from 1-introduction!")


def check_if_symmetric(word):
    length = len(word)
    if length == 0:
        return False

    for i in range(math.floor(length / 2)):
        if word[i] != word[length - 1 - i]:
            return False

    return True


def convert_to_numbers(word):
    arr = []

    for i in range(len(word)):
        arr.append(word_number_map[word[i]])

    return arr


def convert_to_letters(array):
    word = ""

    for num in array:
        word += number_word_map[num]

    return word


def get_intersection(array1, array2):
    dict1 = {}
    result = {}

    for val in array1:
        dict1[val] = True

    for val in array2:
        if val in dict1:
            result[val] = True

    return list(result.keys())


def get_union(array1, array2):
    result = {}

    for val in array1:
        result[val] = True

    for val in array2:
        result[val] = True

    return list(result.keys())


def count_characters(string: str) -> dict:
    result = {}

    for val in string:
        val = val.lower()
        if val in result:
            result[val] = result[val] + 1
        else:
            result[val] = 1

    return result


def is_prime(N: int) -> bool:
    if N <= 1:
        return False

    for n in range(2, math.floor(N / 2) + 1):
        if N % n == 0:
            return False
    return True


if __name__ == "__main__":
    main()
    print(check_if_symmetric("sss"))
    print(convert_to_numbers("a cat"))
    print(convert_to_letters([1, 0, 3, 1, 20]))
    print(get_intersection([1, 2, 4], [3, 1, 9, 2]))
    print(get_union([1, 2, 4], [3, 1, 9, 2]))
    print(count_characters("A cat !!!"))
    print(is_prime(4))
