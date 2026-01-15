"""
matrix_generation.py

Generates matrices and writes them to text files.

Author: Christopher Romo
Created: 2024-02-01
"""


def make_matrix(matrix: list, num_row: int, num_col: int) -> None:
    """
    Initializes a 2D list (matrix) with given number of rows and columns filled
    with zeros.

    Args:
        matrix (list): The 2D list to be initialized.
        num_row (int): The number of rows in the matrix.
        num_col (int): The number of columns in the matrix.
    """

    for i in range(0, num_row):
        col = list()
        for j in range(0, num_col):
            col.append(0)

        matrix.append(col)


def fill_matrix(
    file_name: str, num_row: int, num_col: int, total: int, total_add: int, flip: bool
) -> None:
    """
    Fills a matrix with values and writes it to a file.

    Args:
        file_name (str): The name of the output file.
        num_row (int): The number of rows in the matrix.
        num_col (int): The number of columns in the matrix.
        total (int): The starting value to fill the matrix.
        total_add (int): The value to add for each subsequent element.
        flip (bool): If True, fills the matrix column-wise; if False, fills 
        row-wise.
    """

    file = open(file_name, "w")

    # initialize 2D list
    matrix = list()
    make_matrix(matrix, num_row, num_col)

    # fill 2D list
    if flip:
        for i in range(0, num_col):
            for j in range(0, num_row):
                matrix[j][i] = total
                total += total_add
    else:
        for i in range(0, num_row):
            for j in range(0, num_col):
                total += total_add
                matrix[i][j] = total

    # write matrix to file
    for i in range(0, num_row):
        for j in range(0, num_col):
            the_string = str(matrix[i][j])
            file.write(the_string)
            file.write(" ")

        file.write("\n")

    file.close()


def main() -> None:
    """Program entry point."""

    # fill four matrices with different parameters
    fill_matrix("matrix_1.txt", 4, 11, 0, 1, False)
    fill_matrix("matrix_2.txt", 4, 11, 2, 3, True)
    fill_matrix("matrix_3.txt", 2, 4, 12, -2, False)
    fill_matrix("matrix_4.txt", 4, 2, -6, 1.5, True)


if __name__ == "__main__":
    main()
