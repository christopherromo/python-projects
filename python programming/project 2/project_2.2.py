"""
project_2.2.py

counts the number of characters in a given string, excluding spaces.

author: christopher romo
created: 2023-07-05
"""


def main() -> None:
    """counts the number of characters in a given string, excluding spaces."""

    the_string = input("Please, enter a string: ")
    counter = 0

    # count characters excluding spaces
    for letter in the_string:
        if letter != " ":
            counter += 1

    # print the result
    print("Output: ", end="")
    print(counter)


if __name__ == "__main__":
    main()
