"""
homework_1.1.py

Prints a right triangle of asterisks.

Author: Christopher Romo
Created: 2023-06-21
"""


def printTriangle(size: int) -> None:
    """
    Prints a right triangle of asterisks of given size.

    Args:
        size (int): The size of the triangle.
    """

    base = size

    # build the triangle line by line
    for i in range(size):
        print('*' * base)
        base = base - 1


def main() -> None:
    """Program entry point."""

    # get user input for triangle size
    while True:
        size = int(input('Please, enter the value of n: '))

        if size < 1:
            print('Invalid Input')
        else:
            printTriangle(size)
            break


if __name__ == "__main__":
    main()