"""
program_11.py

Regex example.

Author: Christopher Romo
"""


import re


def main() -> None:
    """Program entry point."""

    # compile a regex to find a pattern of three digits, a hyphen, and three digits
    num_regex = re.compile(r'\d\d\d-\d\d\d')

    # search a string for the pattern
    match_object = num_regex.search('My code is 123-456.')

    # print the found code
    print('Code found: ' + match_object.group())


if __name__ == "__main__":
    main()