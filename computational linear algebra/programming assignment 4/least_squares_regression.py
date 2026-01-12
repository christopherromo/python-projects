"""
least_squares_regression.py

Finds the least squares regression line for a set of coordinates.

Author: Christopher Romo
Created: 2024-04-30
"""


import matplotlib.pyplot as plt
import numpy


def main() -> None:
    """Program entry point."""
    
    # read in the information for coordinate matrix
    input_file = open('coordinates.txt', 'r')
    the_message = input_file.readlines()

    the_list = list()

    for i in range(0,len(the_message)):
        the_list.append(the_message[i].split())

    input_file.close()

    # initialize the coordinate matrix, and create x and y matrices
    x_list = list()
    y_list = list()

    for i in range(0,len(the_list)):
        x_list.append([1,the_list[i][0]])
        y_list.append([the_list[i][1]])

    x_matrix = numpy.array(x_list, dtype=float)
    y_matrix = numpy.array(y_list, dtype=float)

    # create the different matrices and multiply
    x_transposed = numpy.transpose(x_matrix)
    xtx_matrix = numpy.dot(x_transposed,x_matrix)
    xtx_inverse = numpy.linalg.inv(xtx_matrix)
    xty_matrix = numpy.dot(x_transposed,y_matrix)

    # final matrix
    coefficient_matrix = numpy.dot(xtx_inverse,xty_matrix)
    coefficient_matrix = numpy.round(coefficient_matrix, decimals=1)

    x_matrix = numpy.delete(x_matrix,0,1)
    plt.plot(x_matrix, coefficient_matrix[1][0] * x_matrix + coefficient_matrix[0][0])
    plt.plot(x_matrix, y_matrix, 'bo')
    plt.show()

    # output essential data to a file
    least_squares_regression_output = open('least_squares_regression_output.txt', 'w')
    least_squares_regression_output.write('Here are the two coordinate matrices:\n\nx:\n')
    least_squares_regression_output.write(str(x_matrix))
    least_squares_regression_output.write('\n\ny:\n')
    least_squares_regression_output.write(str(y_matrix))
    least_squares_regression_output.write('\n\nHere is the coefficient matrix:\n')
    least_squares_regression_output.write(str(coefficient_matrix))
    least_squares_regression_output.write('\n\nLast but not least, the least squares regression line is:\n')
    least_squares_regression_output.write('y = ' + str(coefficient_matrix[0][0]) + ' + (' + str(coefficient_matrix[1][0]) + 'x)')
    print('\nSuccess! The output file least_squares_regression_output.txt has been created, and the plot has been displayed!\n')

    least_squares_regression_output.close()


if __name__ == "__main__":
    main()