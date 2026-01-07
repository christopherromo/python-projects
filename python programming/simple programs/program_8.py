"""
program_8.py

Numpy and array example.

Author: Christopher Romo
"""


import numpy as np


def main() -> None:
    """Program entry point."""

    dimension = int(input('Enter dimension size: '))

    # create an array of zeros
    checker_board = np.zeros((dimension, dimension))
    checker_board = checker_board.astype(int)

    # fill in the ones for the checkerboard pattern
    checker_board[::2, ::2] = 1
    checker_board[1::2, 1::2] = 1

    # print the checkerboard array
    print(checker_board)


if __name__ == "__main__":
    main()