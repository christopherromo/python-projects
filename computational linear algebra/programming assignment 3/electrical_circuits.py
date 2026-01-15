"""
electrical_circuits.py

Solves for the currents in a given electrical circuit using Kirchhoff's laws.

Author: Christopher Romo
Created: 2024-03-22
"""

import numpy
import sympy


def main() -> None:
    """Program entry point."""

    # the plan

    # node a // i2 = i1 + i3 // -i1 + i2 - i3 = 0
    # node b // i2 = i1 + i4 // -i1 + i2 - i4 = 0
    # node c // i5 = i3 + i6 // -i3 + i5 - i6 = 0
    # node d // i5 = i4 + i6 // -i4 + i5 - i6 = 0
    # top loop    // -i2r2 - i1r1 = e1
    # bottom loop // i5r3 + i6r4 = e2

    # i1,i2,i3,i4,i5,i6,result

    # [[-1,1,-1,0,0,0,0]
    #  [-1,1,0,-1,0,0,0]
    #  [0,0,-1,0,1,-1,0]
    #  [0,0,0,-1,1,-1,0]
    #  [(-1 * r1),(-1 * r2),0,0,0,0,e1]
    #  [0,0,0,0,(1 * r3),(1 * r4),e2]]

    # import the information
    input_file = open("electrical_circuits_input.txt", "r")
    the_message = input_file.readline()
    the_list = the_message.split()

    # resistor and electromagnetic force variables
    r1 = float(the_list[0])
    r2 = float(the_list[1])
    r3 = float(the_list[2])
    r4 = float(the_list[3])
    e1 = float(the_list[4])
    e2 = float(the_list[5])

    input_file.close()

    # create the augmented matrix using the variables above
    augmented_matrix = numpy.array(
        [
            [-1, 1, -1, 0, 0, 0, 0],
            [-1, 1, 0, -1, 0, 0, 0],
            [0, 0, -1, 0, 1, -1, 0],
            [0, 0, 0, -1, 1, -1, 0],
            [(-1 * r1), (-1 * r2), 0, 0, 0, 0, e1],
            [0, 0, 0, 0, (1 * r3), (1 * r4), e2],
        ]
    )

    # create the first output file and add the header and augmented matrix
    electrical_matrices_output = open("electrical_matrices_output.txt", "w")
    electrical_matrices_output.write(
        f"r1: {r1}, r2: {r2}, r3: {r3}, r4: {r4}, e1: {e1}, e2: {e2}"
    )
    electrical_matrices_output.write("\n\nHere is the augmented matrix:\n")
    electrical_matrices_output.write(str(augmented_matrix))

    # get the rref matrix
    the_rref_matrix = sympy.Matrix(augmented_matrix)
    the_rref_matrix = the_rref_matrix.rref()
    the_np_rref_matrix = numpy.array(the_rref_matrix[0], dtype=float)

    # add the rref matrix to the first output file
    electrical_matrices_output.write("\n\nAnd here is the RREF matrix:\n")
    electrical_matrices_output.write(str(the_np_rref_matrix))

    electrical_matrices_output.close()

    # create lists of i6 and current values
    i6_terms = list()
    current_values = list()
    string_list = ["i1", "i2", "i3", "i4", "i5", "i6"]

    # loop through and fill the lists with respective values
    for i in range(0, len(the_np_rref_matrix)):
        i6_terms.append(the_np_rref_matrix[i][5])
        current_values.append(the_np_rref_matrix[i][6])

    # create the second output file and add the header
    electrical_values_output = open("electrical_values_output.txt", "w")
    electrical_values_output.write(
        "Here are all of the currents in terms of i6 (the free variable).\n\n"
    )

    # loop through and print each current value with respect to i6
    for i in range(0, len(the_np_rref_matrix)):
        electrical_values_output.write(
            f"In terms of i6 ({i6_terms[i]}), {string_list[i]}: {current_values[i]}.\n"
        )

    electrical_values_output.close()

    print(
        "\nSuccess! The two output files, electrical_matrices_output.txt and electrical_values_output.txt, have been generated.\n"
    )


if __name__ == "__main__":
    main()
