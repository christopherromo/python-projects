"""
matrix_generation.py

generates matrices and writes them to text files.

author: christopher romo
created: 2024-02-01
"""


def make_matrix(matrix: list, num_row: int, num_col: int) -> None:
    """
    initializes a 2D list (matrix) with given number of rows and columns filled
    with zeros.

    args:
        matrix (list): the 2D list to be initialized.
        num_row (int): the number of rows in the matrix.
        num_col (int): the number of columns in the matrix.
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
    fills a matrix with values and writes it to a file.

    args:
        file_name (str): the name of the output file.
        num_row (int): the number of rows in the matrix.
        num_col (int): the number of columns in the matrix.
        total (int): the starting value to fill the matrix.
        total_add (int): the value to add for each subsequent element.
        flip (bool): if true, fills the matrix column-wise; if false, fills
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
    """generates matrices and writes them to text files."""

    # fill four matrices with different parameters
    fill_matrix("matrix_1.txt", 4, 11, 0, 1, False)
    fill_matrix("matrix_2.txt", 4, 11, 2, 3, True)
    fill_matrix("matrix_3.txt", 2, 4, 12, -2, False)
    fill_matrix("matrix_4.txt", 4, 2, -6, 1.5, True)


if __name__ == "__main__":
    main()
