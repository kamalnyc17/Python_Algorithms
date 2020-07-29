# this program will traverse a list and multiply each items of the list except the current index and
# produce a new list with that total

# importing os and reduce() from functools
import os
from functools import reduce

# initializing variables
my_list, new_list, final_list = [1, 2, 3, 4, 5, 6, 7, 8, 9], [], []

# main loop to traverse through array
for item in my_list:
    new_list = list(filter(lambda i: i != item, my_list))
    final_list.append(reduce(lambda a, b: a*b, new_list))

# clearing the screen and printing final result
os.system('cls' if os.name == 'nt' else 'clear')
print("Total of all items in the base list except the current index")
print("===========================================================")
print(f"The New List: {final_list}")
