# Given a sentence and the position of an open parenthesis, this function
# will find the position of the correcponding close parenthesis
import os
my_sentence = "This is (a beautiful (summer day). It is an ideal (day for (being outdoor (and) playing) games) with) kids."


def find_closing_paren(sentence, opening_position):
    total_open_paren = 0

    # traversing the sentence from the "opening_position" till the position of the corresponding closing
    # parenthesis or the end of the sentence, which ever comes first
    for position in range(opening_position, len(sentence)):
        char = sentence[position]
        if char == '(':
            total_open_paren += 1
        elif char == ')':
            total_open_paren -= 1
            if total_open_paren == 0:
                return position

    return 'No closing parenthesis'


# clear the screen and display result
os.system('cls' if os.name == 'nt' else 'clear')
print(
    f'The location of the corresponding close parenthesis is: {find_closing_paren(my_sentence, 8)}')
