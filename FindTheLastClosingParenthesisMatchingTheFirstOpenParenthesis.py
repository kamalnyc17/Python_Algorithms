# for a given string this program will find the matching closing parenthesis for the very first open parenthesis
# the program will be provided with two parameters, the sentence and the first position of the open parenthesis
input_sentence = "Hi There, (This is just a (sample input sentence (you can change it (any time)) to test) the) logic"

# user defined function to find correct closing parenthesis


def find_closing_parenthesis(strInput, first_position):
    open_parens_count = 0
    # looping through the entire sentence
    for position in range(first_position+1, len(strInput)):
        char = strInput[position]

        if char == "(":
            open_parens_count += 1
        elif char == ")":
            open_parens_count -= 1
            if open_parens_count == 0:
                return position

    return "NOT FOUND"


print(
    f"The location of the closing parenthesis: {find_closing_parenthesis(input_sentence, 9)}")
