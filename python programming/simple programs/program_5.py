"""
program_5.py

Threading and time example.

Author: Christopher Romo
"""


import threading, time


def sum(num_one: int, num_two: int, num_three: int) -> None:
    """
    Sums three numbers after a delay.
    
    Args:
        num_one: The first number.
        num_two: The second number.
        num_three: The third number.
    """

    # wait for 5 seconds before summing and printing the result
    time.sleep(5)
    result = num_one + num_two + num_three
    print(result)


def main() -> None:
    """Program entry point."""

    print('Start of main')

    # create and start the thread
    function_thread = threading.Thread(target=sum, args=[1,2,3])
    function_thread.start()

    print('End of main')


if __name__ == "__main__":
    main()