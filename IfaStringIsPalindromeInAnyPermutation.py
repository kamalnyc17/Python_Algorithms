# this program will take a string and check if it's a Palindrome
# in any permutation
# example of Palindrome: Anna, Madma, Raccare, Teetn
import os
input_string = "Raccare"


def check_palindrome(new_string):
    result = set()
    lower_case_string = new_string.lower()
    # traversing through input string
    for char in lower_case_string:
        if char in result:
            result.remove(char)
        else:
            result.add(char)

    return (len(result) <= 1)


# checking for palindrom
result = f"String {input_string} is a Palindrome" if (check_palindrome(
    input_string)) else f"String {input_string} is NOT a Palindrome"

# printing result
os.system('cls' if os.name == 'nt' else 'clear')
print(result)
