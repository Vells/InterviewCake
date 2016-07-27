"""
Problem 31: Write a recursive function for generating all
permutations of an input string. Return them as a set.
"""


def get_permutations(a_string):

    # base case
    if len(a_string) <= 1:
        return set(a_string)

    substring = a_string[:-1]
    last_char = a_string[-1]

    all_substring_perms = get_permutations(substring)
    all_perms = set()

    for each_perm in all_substring_perms:
        for position in range(len(each_perm) + 1):
            new = "{0}{1}{2}".format(each_perm[:position], last_char, each_perm[position:])
            all_perms.add(new)

    return all_perms


permutations = get_permutations("cats")
print permutations
print "Number of permutations: {0}".format(len(permutations))
