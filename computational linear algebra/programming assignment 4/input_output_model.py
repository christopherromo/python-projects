"""
input_output_model.py

Implements the input-output model to find the total output required to satisfy 
external demand.

Author: Christopher Romo
Created: 2024-04-30
"""

import numpy


def main() -> None:
    """Program entry point."""

    # read in the information for both matrices
    input_file_1 = open("d_matrix_input.txt", "r")
    the_message_1 = input_file_1.readlines()

    the_list_1 = list()

    for i in range(0, 3):
        the_list_1.append(the_message_1[i].split())

    input_file_1.close()

    input_file_2 = open("e_matrix_input.txt", "r")
    the_message_2 = input_file_2.readlines()

    the_list_2 = list()

    for i in range(0, 3):
        the_list_2.append(the_message_2[i].split())

    input_file_2.close()

    # initialize numpy arrays
    d_matrix = numpy.array(the_list_1, dtype=float)
    e_matrix = numpy.array(the_list_2, dtype=float)

    # initialize the identity matrix
    identity_matrix = numpy.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    # subtract the d_matrix from the identity matrix
    id_matrix = identity_matrix - d_matrix

    # find the inverse of the id_matrix and round
    inverse_matrix = numpy.linalg.inv(id_matrix)
    inverse_matrix = numpy.round(inverse_matrix, decimals=2)

    # find the dot product of the inverse_matrix and the e_matrix and round
    x_matrix = numpy.dot(inverse_matrix, e_matrix)
    x_matrix = numpy.round(x_matrix, decimals=1)

    # output essential data to a file
    input_output_matrices_output = open("input_output_matrices_output.txt", "w")
    input_output_matrices_output.write("Here are the two input matrices:\n\nd:\n")
    input_output_matrices_output.write(str(d_matrix))
    input_output_matrices_output.write("\n\ne:\n")
    input_output_matrices_output.write(str(e_matrix))
    input_output_matrices_output.write("\n\nAnd here is the result matrix:\n")
    input_output_matrices_output.write(str(x_matrix))
    input_output_matrices_output.write(
        "\n\nWith A, B, and C corresponding to row 1, 2, and 3.\n"
    )
    print(
        "\nSuccess! The output file input_output_matrices_output.txt has been created!\n"
    )

    input_output_matrices_output.close()


if __name__ == "__main__":
    main()
