"""
program_5.py

threading and time example.

author: christopher romo
"""

import threading, time


def sum(num_one: int, num_two: int, num_three: int) -> None:
    """
    sums three numbers after a delay.

    args:
        num_one (int): the first number.
        num_two (int): the second number.
        num_three (int): the third number.
    """

    # wait for 5 seconds before summing and printing the result
    time.sleep(5)
    result = num_one + num_two + num_three
    print(result)


def main() -> None:
    """threading and time example."""

    print("Start of main")

    # create and start the thread
    function_thread = threading.Thread(target=sum, args=[1, 2, 3])
    function_thread.start()

    print("End of main")


if __name__ == "__main__":
    main()
