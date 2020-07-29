# This is a recursive function for generating all permutations of an input string.
# Assume all charecters are in the string is unique and return them as a set.
import os
input_string = "fat"


def get_permutations(string):
    # Base case
    if len(string) <= 1:
        return set([string])

    all_chars_except_last = string[:-1]
    last_char = string[-1]
    # Recursive call: get all possible permutations for all chars except last
    permutations_of_all_chars_except_last = get_permutations(
        all_chars_except_last)

    # Put the last char in all possible positions for each of
    # the above permutations
    permutations = set()
    for permutation_item in permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = (
                permutation_item[:position]
                + last_char
                + permutation_item[position:]
            )
            permutations.add(permutation)
    return permutations


# clear screen and print output
os.system('cls' if os.name == 'nt' else 'clear')
print(
    f"All possible permutation of the input string is: {get_permutations(input_string)}")
