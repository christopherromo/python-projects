"""
project_1.3.py

prints all characters that appear more than once in a given string.

author: christopher romo
created: 2023-06-21
"""


def main() -> None:
    """prints all characters that appear more than once in a given string."""

    # assumes input is a string
    the_original_string = input("Input: ")
    the_string = the_original_string.lower()
    the_dict = dict()

    # iterate through the string to count occurrences of each character
    for char in the_string:
        if char in the_dict.keys():
            the_dict[char] += 1
        else:
            the_dict[char] = 1

    # print characters that appear more than once
    for key, value in the_dict.items():
        if value > 1:
            print(key, end=" ")


if __name__ == "__main__":
    main()
