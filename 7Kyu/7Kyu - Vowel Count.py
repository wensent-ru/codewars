"""
Vowel Count

Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces.
"""


def get_count_first(sentence):
    return sum(c in 'aeiou' for c in sentence)


def get_count_second(sentence):
    count = 0
    for i in sentence:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            count += 1
    return count
