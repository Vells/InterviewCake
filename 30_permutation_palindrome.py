# coding=utf-8
import json


"""
Problem #30

Write an efficient function that checks whether
any permutation of an input string is a palindrome.

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
        odd_counts += 1 if count % 2 else 0

    print "letter_counts: {0}".format(json.dumps(letter_counts, indent=4))
    return odd_counts == 1


def permutation_palindrome(word):
    """
    Time complexity: O(n) where n is the length of the word
    Space complexity: O(n) - size of the set unpaired_chars
        but since there is a limited number of unique characters in both the
        Unicode and ASCII char sets, we might want to say that space complexity is O(1)
    """
    unpaired_characters = set()

    for letter in word:
        if letter in unpaired_characters:
            unpaired_characters.remove(letter)
        else:
            unpaired_characters.add(letter)

    return len(unpaired_characters) <= 1


assert permutation_palindrome_1("civic") is True
assert permutation_palindrome_1("ivicc") is True
assert permutation_palindrome_1("civil") is False
assert permutation_palindrome_1("livci") is False
