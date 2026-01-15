"""
matrix_addition.py

Adds two matrices selected by the user and outputs the result to a file.

Author: Christopher Romo
Created: 2024-02-01
"""


def main() -> None:
    """Program entry point."""

    mat1_selected = False
    mat2_selected = False
    mat3_selected = False
    mat4_selected = False

    print("Please select Matrix #1: Mat1, Mat2, Mat3, or Mat4")

    # find the first matrix to be used
    choice_made = False

    while choice_made == False:
        input_string = input()

        if input_string == "Mat1":
            mat1_selected = True
            choice_made = True
            mata_file = open("matrix_1.txt", "r")
        elif input_string == "Mat2":
            mat2_selected = True
            choice_made = True
            mata_file = open("matrix_2.txt", "r")
        elif input_string == "Mat3":
            mat3_selected = True
            choice_made = True
            mata_file = open("matrix_3.txt", "r")
        elif input_string == "Mat4":
            mat4_selected = True
            choice_made = True
            mata_file = open("matrix_4.txt", "r")
        else:
            print("Error! Please enter Mat1, Mat2, Mat3 or Mat4")

    # prompt for second matrix
    if mat1_selected == True:
        print("Please select Matrix #2: Mat2, Mat3, or Mat4")
    elif mat2_selected == True:
        print("Please select Matrix #2: Mat1, Mat3, or Mat4")
    elif mat3_selected == True:
        print("Please select Matrix #2: Mat1, Mat2, or Mat4")
    elif mat4_selected == True:
        print("Please select Matrix #2: Mat1, Mat2, or Mat3")

    # find the second matrix to be used
    choice_made = False

    while choice_made == False:
        input_string = input()

        if input_string == "Mat1":
            if mat1_selected == True:
                print(
                    "You have already selected this matrix! Please enter Mat2, Mat3, or Mat4"
                )
            else:
                mat1_selected = True
                choice_made = True
                matb_file = open("matrix_1.txt", "r")
        elif input_string == "Mat2":
            if mat2_selected == True:
                print(
                    "You have already selected this matrix! Please enter Mat1, Mat3, or Mat4"
                )
            else:
                mat2_selected = True
                choice_made = True
                matb_file = open("matrix_2.txt", "r")
        elif input_string == "Mat3":
            if mat3_selected == True:
                print(
                    "You have already selected this matrix! Please enter Mat1, Mat2, or Mat4"
                )
            else:
                mat3_selected = True
                choice_made = True
                matb_file = open("matrix_3.txt", "r")
        elif input_string == "Mat4":
            if mat4_selected == True:
                print(
                    "You have already selected this matrix! Please enter Mat1, Mat2, or Mat3"
                )
            else:
                mat4_selected = True
                choice_made = True
                matb_file = open("matrix_4.txt", "r")
        else:
            if mat1_selected == True:
                print("Error! Please enter Mat2, Mat3, or Mat4")
            elif mat2_selected == True:
                print("Error! Please enter Mat1, Mat3, or Mat4")
            elif mat3_selected == True:
                print("Error! Please enter Mat1, Mat2, or Mat4")
            elif mat4_selected == True:
                print("Error! Please enter Mat1, Mat2, or Mat3")

    # read the lines, and find number of rows
    mata_lines = mata_file.readlines()
    matb_lines = matb_file.readlines()

    mata_num_rows = len(mata_lines)
    matb_num_rows = len(matb_lines)

    # populate both 2D lists
    mata = list()

    for i in range(0, mata_num_rows):
        col = mata_lines[i].split()
        mata.append(col)

    matb = list()

    for i in range(0, matb_num_rows):
        col = matb_lines[i].split()
        matb.append(col)

    # find number of columns
    mata_num_col = len(mata[0])
    matb_num_col = len(matb[0])

    # find which matrix has the minimum amount rows/columns
    row_count = 0

    if mata_num_rows < matb_num_rows:
        row_count = mata_num_rows
    else:
        row_count = matb_num_rows

    col_count = 0

    if mata_num_col < matb_num_col:
        col_count = mata_num_col
    else:
        col_count = matb_num_col

    # create and populate added 2D list
    added_mat = list()

    for i in range(0, row_count):
        col = list()
        for j in range(0, col_count):
            added_num = float(mata[i][j]) + float(matb[i][j])

            if str(added_num).endswith(".0"):
                added_num = int(added_num)

            col.append(added_num)

        added_mat.append(col)

    # export to file
    if mat1_selected == True:
        if mat2_selected == True:
            output_file = "matrix_output_1_2.txt"
        elif mat3_selected == True:
            output_file = "matrix_output_1_3.txt"
        elif mat4_selected == True:
            output_file = "matrix_output_1_4.txt"
    elif mat2_selected == True:
        if mat3_selected == True:
            output_file = "matrix_output_2_3.txt"
        elif mat4_selected == True:
            output_file = "matrix_output_2_4.txt"
    elif mat3_selected == True:
        if mat4_selected == True:
            output_file = "matrix_output_3_4.txt"

    added_mat_file = open(output_file, "w")

    for i in range(0, row_count):
        for j in range(0, col_count):
            the_string = str(added_mat[i][j])
            added_mat_file.write(the_string)
            added_mat_file.write(" ")
        added_mat_file.write("\n")

    print("The added matrix file has been generated.")

    mata_file.close()
    matb_file.close()
    added_mat_file.close()


if __name__ == "__main__":
    main()
