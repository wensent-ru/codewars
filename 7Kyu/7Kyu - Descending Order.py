"""
Descending Order

Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in
descending order. Essentially, rearrange the digits to create the highest possible number.
"""


def descending_order(num):
    sorted_list = [x for x in str(num)]
    sorted_list.sort(reverse=True)
    return int("".join([str(x) for x in sorted_list]))
