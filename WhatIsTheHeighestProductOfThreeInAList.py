# Given a list of integers, this program will find the highest product we can get from three of the integers.
# The list must contain at least 3 integers (either positive or negative)
import os
int_list = [2, -5, 10, 7, 15, 17, -110, 9]

# user defined function to perform calculation


def find_highest_product_of_3(list_of_ints):

    if len(list_of_ints) < 3:
        raise ValueError('The list contains less than 3 items!')

    # We're going to start at index 2 i.e. the 3rd item and
    # pre-populate highest and lowest based on the first 2 items of the list.
    highest_number = max(list_of_ints[0], list_of_ints[1])
    lowest_number = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]

    # now we pre-populate the highest_product_of_3 with the first three items.
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # traverse through the list, starting at index 2
    for i in range(2, len(list_of_ints)):
        current_int = list_of_ints[i]

        # finding new highest product of three
        highest_product_of_3 = max(highest_product_of_3, current_int * highest_product_of_2,
                                   current_int * lowest_product_of_2)

        # checking for new highest product of two
        highest_product_of_2 = max(highest_product_of_2, current_int * highest_number,
                                   current_int * lowest_number)

        # checking for new highest product of two
        lowest_product_of_2 = min(lowest_product_of_2, current_int * highest_number,
                                  current_int * lowest_number)

        # check if the current int is the new highest
        highest_number = max(highest_number, current_int)

        # check if the current int is the new lowest
        lowest_number = min(lowest_number, current_int)

    return highest_product_of_3


# clear screen and display output
os.system('cls' if os.name == 'nt' else 'clear')
print(
    f"Highest product of three of this list: {find_highest_product_of_3(int_list)}")
