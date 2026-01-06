"""
homework_1.2.py

Checks if a list contains three consecutive identical numbers.
Assumes input is in the form of a list of integers: [1,2,3]

Author: Christopher Romo
Created: 2023-06-21
"""


def main() -> None:
    """Program entry point."""

    the_original_string = input('Input: ')      # get user input
    the_string = the_original_string[1:-1]      # gets rid of square brackets
    the_list = the_string.split(',')            # turns string into list

    is_consecutive = False
    repeat_count = 1
    last_number = None

    # iterate through the list to check for three consecutive identical numbers
    for element in the_list:
        if element == last_number:
            repeat_count = repeat_count + 1
        else:
            repeat_count = 1

        last_number = element

        if repeat_count == 3:
            is_consecutive = True

    # print the result
    if is_consecutive:
        print('Output: True')
    else:
        print('Output: False')


if __name__ == "__main__":
    main()