"""
merge_sort.py

Performs merge sort on a list of numbers.

Author: Christopher Romo
Created: 2024-02-08
"""


import time


def merge_sort(a_list: list) -> list:
    """
    Performs merge sort on a list of numbers.

    Args:
        a_list: The list of numbers to be sorted.

    Returns:
        The sorted list of numbers.
    """

    a_list_len = len(a_list)

    # base case
    if a_list_len <= 1:
        return a_list
    else:
        # find the middle of the list to split it
        midpoint = a_list_len // 2

        # initialize the separate lists
        first_list = list()
        second_list = list()

        # populate the first list with the first half of the incoming list
        for i in range(0, midpoint):
            first_list.append(a_list[i])

        # populate the second list with the second half of the incoming list
        for i in range(midpoint, a_list_len):
            second_list.append(a_list[i])

        # recursive call on both lists
        first_list = merge_sort(first_list)
        second_list = merge_sort(second_list)

        # initialize return list
        return_list = list()

        # counters for both lists
        i = 0
        j = 0

        # boolean variables representing if all values in the two lists have been added to return list
        first_list_empty = False
        second_list_empty = False

        # while both lists have values to add to the return list
        while first_list_empty == False and second_list_empty == False:
            if i == len(first_list):                
                # terminate loop by switching boolean
                first_list_empty = True
            elif j == len(second_list):             
                # terminate loop by switching boolean
                second_list_empty = True
            elif first_list[i] < second_list[j]:    
                # append value to return list and increment i
                return_list.append(first_list[i])
                i += 1
            else:                                   
                # append value to return list and increment j
                return_list.append(second_list[j])
                j += 1

        # if first list is not empty, add remaining values to return list
        while first_list_empty == False:
            if i == len(first_list):                
                # terminate loop by switching boolean
                first_list_empty = True
            else:
                return_list.append(first_list[i])
                i += 1

        # if second list is not empty, add remaining values to return list
        while second_list_empty == False:
            if j == len(second_list):               
                # terminate loop by switching boolean
                second_list_empty = True
            else:
                return_list.append(second_list[j])
                j += 1
        
        # return the list
        return return_list
        

def main() -> None:
    """Program entry point."""

    # read in the list from a file and grab the length
    input_file = open('sort_list3_input.txt', 'r')

    the_list = input_file.readlines()
    the_list_len = len(the_list)

    # go through the list and strip the newline characters
    for i in range(0, the_list_len):
        the_list[i] = str(the_list[i]).strip()
        the_list[i] = int(the_list[i])

    # print pre-sort list
    print('Pre-Sort:')
    print(the_list)  
        
    # calls the function and tracks time
    time_before = time.time()
    nano_time_before = time.time_ns()

    the_list = merge_sort(the_list)

    time_after = time.time()
    nano_time_after = time.time_ns()

    # finds the time it took to get an answer
    time_elapsed = time_after - time_before
    nano_time_elapsed = nano_time_after - nano_time_before

    # print post-sort list and time
    print('Post-Sort:')
    print(the_list)
    print(f"Time Elapsed in Seconds: {time_elapsed}")
    print(f"Time Elapsed in Nanoseconds: {nano_time_elapsed}")
    print(f"n: {the_list_len}")


if __name__ == "__main__":
    main()