"""
graphic_transformations.py

Draws the letter 'A' and applies graphic transformations based on user input.

Author: Christopher Romo
Created: 2024-03-19
"""

import turtle
import numpy
import math


def format_matrix(the_array: numpy.array) -> numpy.array:
    """
    Formats the input array to reorder the columns for drawing the letter 'A'.

    Args:
        the_array (numpy.array): A 3xN array where each column represents a
        point (x, y, 1).

    Returns:
        numpy.array: A reformatted 3xN array with columns ordered for drawing.
    """

    # use placeholders for swapping the columns
    a1 = the_array[0][0]
    a2 = the_array[0][1]
    a3 = the_array[0][2]
    a4 = the_array[0][3]
    a5 = the_array[0][4]
    b1 = the_array[1][0]
    b2 = the_array[1][1]
    b3 = the_array[1][2]
    b4 = the_array[1][3]
    b5 = the_array[1][4]

    formatted_matrix = numpy.array(
        [[a1, a4, a5, a3, a2], [b1, b4, b5, b3, b2], [1, 1, 1, 1, 1]]
    )

    return formatted_matrix


def draw_a(the_array: numpy.array) -> None:
    """
    Draws the letter 'A' based on the provided 2D array of points with columns
    formatted in the order: 1, 4, 5, 3, 2.

    Args:
        the_array (numpy.array): A 3xN array where each column represents a
        point (x, y, 1).
    """

    for i in range(0, len(the_array[0])):
        # find current coordinates
        x_cord = the_array[0][i]
        y_cord = the_array[1][i]

        # handle last value in row, otherwise find the next coordinate
        if i == (len(the_array[0]) - 1):
            x_cord = the_array[0][i - 1]
            y_cord = the_array[1][i - 1]
            next_x = the_array[0][i - 3]
            next_y = the_array[1][i - 3]
        else:
            next_x = the_array[0][i + 1]
            next_y = the_array[1][i + 1]

        # scale by ten for visibility
        x_cord = x_cord * 10
        y_cord = y_cord * 10
        next_x = next_x * 10
        next_y = next_y * 10

        # draw the line
        turtle.penup()
        turtle.goto(x_cord, y_cord)
        turtle.pendown()
        turtle.goto(next_x, next_y)
        turtle.penup()


def main() -> None:
    """Program entry point."""

    # import the information
    input_file = open("graphic_transformation1_input.txt", "r")
    the_message = input_file.readline()
    the_list = the_message.split()

    # assign information
    point_x = float(the_list[0])
    point_y = float(the_list[1])
    rotation = float(the_list[2])
    x_shear = float(the_list[3])
    x_scale = float(the_list[4])
    order = the_list[5]

    input_file.close()

    # original letter a matrix
    letter_a = numpy.array([[0, 6, 5, 1, 3], [0, 0, 3, 3, 9], [1, 1, 1, 1, 1]])

    # format matrix and draw the letter
    formatted_matrix = format_matrix(letter_a)
    draw_a(formatted_matrix)

    # create letter a output file and add original matrix
    graphic_transformation_output = open("graphic_transformation_output.txt", "w")
    graphic_transformation_output.write("Here is the original letter a matrix:\n")
    graphic_transformation_output.write(str(letter_a))

    # create composite output file
    graphic_composite_output = open("graphic_composite_output.txt", "w")
    graphic_composite_output.write(
        "Here are the matrices used to make the transformations:"
    )
    composite_matrix = numpy.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

    # apply transformations in the correct order
    for num in order:
        match num:
            # rotations
            case "1":
                # create matrices to be used
                move_to_origin_matrix = numpy.array(
                    [[1, 0, (point_x * -1)], [0, 1, (point_y * -1)], [0, 0, 1]]
                )
                move_back_from_origin_matrix = numpy.array(
                    [[1, 0, point_x], [0, 1, point_y], [0, 0, 1]]
                )
                rotation_matrix = numpy.array(
                    [
                        [math.cos(rotation), (math.sin(rotation) * -1), 0],
                        [math.sin(rotation), math.cos(rotation), 0],
                        [0, 0, 1],
                    ]
                )

                # multiply letter matrix
                letter_a = numpy.dot(move_to_origin_matrix, letter_a)
                letter_a = numpy.dot(rotation_matrix, letter_a)
                letter_a = numpy.dot(move_back_from_origin_matrix, letter_a)

                # add matrices to composite file and multiply with composite
                # matrix
                graphic_composite_output.write("\n\nRotation Matrix:\n")
                graphic_composite_output.write(str(rotation_matrix))
                composite_matrix = numpy.dot(rotation_matrix, composite_matrix)
            # shearing
            case "2":
                # create matrix and multiply
                shearing_matrix = numpy.array([[1, x_shear, 0], [0, 1, 0], [0, 0, 1]])
                letter_a = numpy.dot(shearing_matrix, letter_a)

                # add matrix to composite file and multiply with composite
                # matrix
                graphic_composite_output.write("\n\nShearing Matrix:\n")
                graphic_composite_output.write(str(shearing_matrix))
                composite_matrix = numpy.dot(shearing_matrix, composite_matrix)
            # scaling
            case "3":
                # create matrix and multiply
                scaling_matrix = numpy.array([[x_scale, 0, 0], [0, 1, 0], [0, 0, 1]])
                letter_a = numpy.dot(scaling_matrix, letter_a)

                # add matrix to composite file and multiply with composite
                # matrix
                graphic_composite_output.write("\n\nScaling Matrix:\n")
                graphic_composite_output.write(str(scaling_matrix))
                composite_matrix = numpy.dot(scaling_matrix, composite_matrix)
            # end case
            case "0":
                # end the loop if a 0 is detected
                break

    # add the transformed letter a matrix to letter a output file
    graphic_transformation_output.write(
        "\n\nAnd here is the transformed letter a matrix:\n"
    )
    graphic_transformation_output.write(str(letter_a))

    graphic_transformation_output.close()

    # add composite matrix to composite file
    graphic_composite_output.write("\n")
    graphic_composite_output.write("\nComposite Transformation Matrix:\n")
    graphic_composite_output.write(str(composite_matrix))

    graphic_composite_output.close()

    print(
        "\nSuccess! Turtle will now show the transformation, and the two output files,\ngraphic_composite_output.txt and graphic_transformation_output.txt, have been generated.\n"
    )

    # format matrix and draw the letter
    turtle.pencolor("red")
    formatted_matrix = format_matrix(letter_a)
    draw_a(formatted_matrix)
    turtle.exitonclick()


if __name__ == "__main__":
    main()
