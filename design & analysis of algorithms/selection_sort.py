"""
selection_sort.py

Performs selection sort on a list of numbers.

Author: Christopher Romo
Created: 2024-02-08
"""

import time


def main() -> None:
    """Program entry point."""

    # read in the list from a file and grab the length
    # please be aware that sort_list3_input.txt can take a while to sort
    input_file = open("sort_list1_input.txt", "r")

    the_list = input_file.readlines()
    the_list_len = len(the_list)

    input_file.close()

    # go through the list and strip the newline characters
    for i in range(0, the_list_len):
        the_list[i] = str(the_list[i]).strip()
        the_list[i] = int(the_list[i])

    # print pre-sort list
    print("Pre-Sort:")
    print(the_list)

    # performs the selection sort and tracks time
    time_before = time.time()
    nano_time_before = time.time_ns()

    for i in range(0, the_list_len):
        # define smallest index
        index = i

        # for loop for finding the next minimum value
        for j in range(0, the_list_len):
            # if the index we are on is past the sorted list so far
            if j > i:
                # if this number is smaller than the current smallest, save the 
                # index
                if the_list[index] > the_list[j]:
                    index = j

        # swap the current number and the smallest number
        temp = the_list[i]
        the_list[i] = the_list[index]
        the_list[index] = temp

    time_after = time.time()
    nano_time_after = time.time_ns()

    # finds the time it took to get an answer
    time_elapsed = time_after - time_before
    nano_time_elapsed = nano_time_after - nano_time_before

    # print post-sort list and time
    print("Post-Sort:")
    print(the_list)
    print(f"Time Elapsed in Seconds: {time_elapsed}")
    print(f"Time Elapsed in Nanoseconds: {nano_time_elapsed}")
    print(f"n: {the_list_len}")


if __name__ == "__main__":
    main()
