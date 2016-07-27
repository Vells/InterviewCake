# coding=utf-8
import json


"""
Problem #30

For a string of length n, there are n! permutations
(n choices for the first character, times n−1 choices for the second character, etc).
Checking each length-n permutation to see if it's a palindrome involves
checking each character, taking O(n) time. That gives us O(n!n)
"""


def permutation_palindrome_1(word):
    letter_counts = {}

    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    odd_counts = 0
    for count in letter_counts.values():
        odd_counts += 1 if not count % 2 else 0

    print "letter_counts: {0}".format(json.dumps(letter_counts, indent=4))
    return not odd_counts % 2


def permutation_palindrome(word):
    unpaired_characters = set()

    for letter in word:
        if letter in unpaired_characters:
            unpaired_characters.remove(letter)
        else:
            unpaired_characters.add(letter)

    return len(unpaired_characters) <= 1


assert permutation_palindrome("civic") is True
assert permutation_palindrome("ivicc") is True
assert permutation_palindrome("civil") is False
assert permutation_palindrome("livci") is False
