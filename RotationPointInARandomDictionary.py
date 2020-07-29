import os

word_list = [
    'ptolemaic',
    'python',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'zoo',
    'asymptote',
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'mango',
    'othellolagkage',
]

# user defined function


def find_point_of_rotation(words):
    first_word = words[0]
    start_index = 0
    end_index = len(words) - 1

    while start_index < end_index:
        # Guess a point halfway between floor and ceiling
        running_index = start_index + ((end_index - start_index) // 2)

        # If guess comes after first word or is the first word
        if words[running_index] >= first_word:
            # Go right
            start_index = running_index
        else:
            # Go left
            end_index = running_index

        # If floor and ceiling have converged
        if start_index + 1 == end_index:
            # Between floor and ceiling is where we flipped to the beginning
            # so ceiling is alphabetically first
            return end_index


# clear screen and print output
os.system('cls' if os.name == 'nt' else 'clear')
print(
    f"Correct Rotation Point for this dictionary is: {find_point_of_rotation(word_list)}")
