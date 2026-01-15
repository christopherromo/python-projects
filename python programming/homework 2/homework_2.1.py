"""
homework_2.1.py

Replaces the second half of a given string with its uppercase version.

Author: Christopher Romo
Created: 2023-07-05
"""


def main() -> None:
    """Program entry point."""

    counter_one = 0
    counter_two = 0

    the_string = input("Please, enter a word: ")
    the_string.lower()

    the_new_string = ""

    the_length = len(the_string)
    replace_length = int(the_length / 2)
    keep_length = the_length - replace_length

    # build the new string
    while counter_one < keep_length:
        the_new_string = the_new_string + the_string[counter_one]
        counter_one += 1

    # replace the second half with uppercase
    while replace_length > 0:
        counter_two = replace_length * -1
        the_new_string = the_new_string + the_string[counter_two].upper()
        replace_length = replace_length - 1

    # print the result
    print("Output: ", end="")
    print(the_new_string)


if __name__ == "__main__":
    main()
