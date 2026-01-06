"""
homework_2.2.py

Counts the number of characters in a given string, excluding spaces.

Author: Christopher Romo
Created: 2023-07-05
"""


def main() -> None:
    """Program entry point."""

    the_string = input('Please, enter a string: ')
    counter = 0

    # count characters excluding spaces
    for letter in the_string:
        if letter != " ":
            counter += 1

    # print the result
    print('Output: ', end='')
    print(counter)


if __name__ == "__main__":
    main()