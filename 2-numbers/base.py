import math


def find_largest_power_of_base_in_number(num: int, base: int) -> int:
    # cleanest version using log constant time
    # return math.floor(math.log(num, base))
    # second cleanest method, using the principle behind logs
    # we basically divide by the base, then we count the number of times we divide
    # till we get to a point where we can't d
    power = 0
    while num >= base:
        num //= base
        power += 1
    return power

    # this is my worse performing one, as I basically say loop through from 0 to a high enough number
    # then raise the base to the index and check if it's less than or equal to the number
    # this is very inefficient as exponents are expensive, while this works it's not so good.
    # power = 0
    # for i in range(math.floor(num / base)):
    #     if (base ** i) <= num:
    #         power = i
    #     else:
    #         break
    # return power


def binary_to_decimal(string):
    amount = 0

    for i in range(len(string)):
        index = len(string) - 1 - i
        amount = amount + ((2**i) * int(string[index]))
    return amount

def hexadecimal_to_decimal(string):
    return 0


if __name__ == "__main__":
    # print(binary_to_decimal("11010"))
    # print(find_largest_power_of_base_in_number(26, 2))
    # print(find_largest_power_of_base_in_number(241791, 16))
    # print(binary_to_decimal("11010"))
    print(binary_to_decimal("10"))
    # print(45183// 4096)
    # print(241791 // 65536)
