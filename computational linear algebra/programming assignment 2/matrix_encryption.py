"""
matrix_encryption.py

Encodes a secret message using matrix multiplication.

Author: Christopher Romo
Created: 2024-02-20
"""


import numpy


def main() -> None:
    """Program entry point."""

    # import the message to be encoded
    input_file = open('secret_message.txt', 'r')
    the_message = input_file.readline()

    input_file.close()
    
    # create a list of the unicode numbers
    the_list = list()

    for char in the_message:
        unicode_of_char = ord(char)
        the_list.append(unicode_of_char)

    # fill the remaining spots with zero
    while len(the_list) % 4 != 0:
        the_list.append(0)

    num_cols = len(the_list) // 4

    # create the matrix and shape it
    the_matrix = numpy.array(the_list)
    the_matrix = numpy.reshape(the_matrix, (4, num_cols), order = 'F')

    # create the encoding matrix
    encoding_matrix = numpy.array([[1,-1,-1,1], [2,-3,-5,4], [-2,-1,-2,2], [3,-3,-1,2]])

    # multiply the two matrices to receive encoded matrix
    encoded_matrix = numpy.dot(encoding_matrix, the_matrix)

    # print the matrices to the console
    print('Encoding Matrix:')
    print(encoding_matrix)
    print()
    print('Plaintext Matrix:')
    print(the_matrix)
    print()
    print('Encoded Matrix:')
    print(encoded_matrix)

    # output the matrix to a file
    output_file = open('encoded_matrix.txt', 'w')

    for i in range(0, 4):
        for j in range(0, num_cols):
            output_file.write(str(encoded_matrix[i][j]))
            output_file.write(' ')

    output_file.close()


if __name__ == "__main__":
    main()