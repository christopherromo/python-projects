"""
matrix_decryption.py

Decodes a secret message encoded with matrix multiplication.

Author: Christopher Romo
Created: 2024-02-22
"""


import numpy


def main() -> None:
    """Program entry point."""

    # import the encoded numbers
    input_file = open('encoded_matrix.txt', 'r')
    the_message = input_file.readline()

    input_file.close()
    
    # transfer from the string to a list
    the_message = the_message.split()
    the_list = list()

    counter = 0

    for num in the_message:
        the_list.append(int(num))
        counter += 1

    counter = counter // 4

    # create the matrix and shape it back into it's original position
    encoded_matrix = numpy.array(the_list)
    encoded_matrix = numpy.reshape(encoded_matrix, (4,counter))

    # create inverse matrix
    inverse_matrix = numpy.array([[6,-1,0,-1], [22,-4,1,-4], [14,-3,1,-2], [31,-6,2,-5]])

    # multiply the two matrices to receive plaintext matrix
    the_matrix = numpy.dot(inverse_matrix, encoded_matrix)

    # print the matrices to the console
    print('Inverse of Encoding Matrix:')
    print(inverse_matrix)
    print()
    print('Encoded Matrix:')
    print(encoded_matrix)
    print()
    print('Plaintext Matrix:')
    print(the_matrix)
    print()

    # transfer back to an array
    matrix_size = the_matrix.size
    the_matrix = numpy.reshape(the_matrix, matrix_size, order='F')

    # make the array into a list
    the_new_list = the_matrix.tolist()

    # iterate through list and receive original message
    the_string = ''

    for num in the_new_list:
        the_string += chr(num)

    print('Original Message:')
    print(the_string)


if __name__ == "__main__":
    main()