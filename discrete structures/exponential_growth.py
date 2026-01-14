"""
exponential_growth.py

Exercises involving exponential growth and timing functions.

Author: Christopher Romo
"""


import time


def expect_equal(a: any, b: any) -> None:
    """
    Compares two values and prints a message if they are not equal.

    Args:
        a (any): The first value.
        b (any): The second value.
    """

    if a != b: print('FAIL expected:', b, ' got:', a)


def a_to_the_b(a: int, b: int) -> int:
    """
    Counts to a^b using a loop.

    Args:
        a (int): The base.
        b (int): The exponent.

    Returns:
        int: The count up to a^b.
    """
  
    count = 0
    
    while count < pow(a,b):
        count += 1
    
    return count


def time_the_function(a: int, b: int) -> float:
    """
    Times how long it takes to run a_to_the_b(a,b).

    Args:
        a (int): The base.
        b (int): The exponent.

    Returns:
        float: The time taken to run a_to_the_b(a,b).
    """

    time_before = time.time()
    a_to_the_b(a,b)
    time_after = time.time()

    time_elapsed = time_after - time_before
    
    return time_elapsed


def main() -> None:
    """Program entry point."""

    # originally a jupyter notebook exercise

    # task 1

    # Implement the following pseudocode as the function a_to_the_b(a,b) in the cell below:
    # 1. Initialize count = 0.
    # 2. Repeat the following line as long as count is less than a^b:
    # 3. Increment count by 1.
    # 4. Return count.

    expect_equal(a_to_the_b(1,1),1)
    expect_equal(a_to_the_b(4,3),pow(4,3))
    expect_equal(a_to_the_b(4554,2),4554*4554)

    # task 2

    # Your function should accept arguments a and b, pass them to
    # a_to_the_b(a,b), and then return the amount of time it took to run.

    print("task 2 output:")
    print('If your function is working properly, each of the following numbers should be close to 2:')
    print(time_the_function(1414,2)/time_the_function(1000,2))
    print(time_the_function(2,15)/time_the_function(2,14))
    print('\nIf the numbers jump around but always come back to 2, that is a good sign.\nIf they are always above 4 or below 1.5, that means something is probably wrong.')
    print()

    # task 3

    # What you'll do: write code that prints the running time (as returned by time_the_function(a,b) that you
    # created above) of several polynomial functions, with various numbers held constant and others changing.
    # Write code which prints out 3 lists on the screen. Each list should have entries as described below.
    # List 1: the time it takes your function to count to n^2 for each n in {100x: x in {1,2,3,4,5,6,7,8,9,10}}.
    # List 2: the time it takes your function to count to n^3 for each n in {20x: x in {1,2,3,4,5,6,7,8,9,10}}.
    # List 3: the time it takes your function to count to n^5 for each n in {2x: x in {1,2,3,4,5,6,7,8,9,10}}.

    print("task 3 output:")

    # your code here for List 1
    for x in range(1,11):
        n = x * 100
        total_time = time_the_function(n, 2)
        print(f"Time to count to {n}^2: {total_time}")

    print()

    # your code here for List 2
    for x in range(1,11):
        n = x * 20
        total_time = time_the_function(n, 3)
        print(f"Time to count to {n}^3: {total_time}")

    print()

    # your code here for List 3
    for x in range(1,11):
        n = x * 2
        total_time = time_the_function(n, 5)
        print(f"Time to count to {n}^5: {total_time}")

    print()

    # task 4

    # Instructions:
    # 1. You may figure out the answer in any way you want (either by plugging numbers in by hand [recommended],
    # or by writing code which figures out the answer itself).
    # 2. Once you figure out your answer, your should report your results by giving a line of code which prints
    # time_the_function for the largest n which takes less than 3 seconds to run. We should be able to read your
    # code's output to see what number you plugged in!
    # 3. If you wrote code to figure out the answer, DO NOT submit that code because that will make your notebook run forever.
    # 4. Finally, include a text cell or a code comment that says how much higher you could go before it ran over 3
    # seconds. For example, the highest number in list 1 is 1000; if you could go all the way up to 5000 before it
    # hit 3 seconds, then say "I could go 4000 higher."

    print("task 4 output:")

    # How much higher can you go (approximately) on List 1 with n^2 before the function takes 3 seconds to run?
    n = 4650
    total_time = time_the_function(n, 2)
    print(f"The number I plugged in was {n}, and the time was {total_time}. So, I could go 3650 higher.")

    # How much higher can you go (approximately) on List 2 with n^3 before the function takes 3 seconds to run?
    n = 260
    total_time = time_the_function(n, 3)
    print(f"The number I plugged in was {n}, and the time was {total_time}. So, I could go 60 higher.")

    # How much higher can you go (approximately) on List 3 with n^5 before the function takes 3 seconds to run?
    n = 28
    total_time = time_the_function(n, 5)
    print(f"The number I plugged in was {n}, and the time was {total_time}. So, I could go 8 higher.")

    print()

    # task 5

    # What you'll do: write code that prints the running time (as returned by time_the_function(a,b) that you created above)
    # of several exponential functions, with various numbers held constant and others changing.
    # Write code which prints out 3 lists on the screen. Each list should have entries as described below. Note that these
    # exponential functions have pretty small bases (1.015, 1.08, 2); they're pretty gentle as far as exponential functions go.
    # List 1: the time it takes your function to count to 1.015^n for each n in {100x: x in {1,2,3,4,5,6,7,8,9,10}}.
    # List 2: the time it takes your function to count to 1.08^n for each n in {20x: x in {1,2,3,4,5,6,7,8,9,10}}.
    # List 3: the time it takes your function to count to 2^n for each n in {2x: x in {1,2,3,4,5,6,7,8,9,10}}.

    print("task 5 output:")

    # your code here for List 1
    for x in range(1,11):
        n = x * 100
        total_time = time_the_function(1.015, n)
        print(f"Time to count to 1.015^{n}: {total_time}")

    print()

    # your code here for List 2
    for x in range(1,11):
        n = x * 20
        total_time = time_the_function(1.08, n)
        print(f"Time to count to 1.08^{n}: {total_time}")

    print()

    # your code here for List 3
    for x in range(1,11):
        n = x * 2
        total_time = time_the_function(2, n)
        print(f"Time to count to 2^{n}: {total_time}")

    print()

    # task 6

    # Instructions:
    # 1. You may figure out the answer in any way you want (either by plugging numbers in by hand [recommended],
    # or by writing code which figures out the answer itself).
    # 2. Once you figure out your answer, your should report your results by giving a line of code which prints
    # time_the_function for the largest n which takes less than 3 seconds to run. We should be able to read
    # your code's output to see what number you plugged in!
    # 3. If you wrote code to figure out the answer, DO NOT submit that code because that will make your notebook 
    # run forever.
    # 4. Finally, include a text cell or a code comment that says how much higher you could go before it ran over
    # 3 seconds. For example, the highest number in list 1 is 1000; if you could go all the way up to 5000 before
    # it hit 3 seconds, then say "I could go 4000 higher."
    
    print("task 6 output:")

    # How much higher can you go (approximately) on List 1 with 1.015^n before the function takes 3 seconds to run?
    n = 1070
    total_time = time_the_function(1.015, n)
    print(f"The number I plugged in was {n}, and the time was {total_time}. So, I could go 70 higher.")

    # How much higher can you go (approximately) on List 2 with 1.08^n before the function takes 3 seconds to run?
    n = 207
    total_time = time_the_function(1.08, n)
    print(f"The number I plugged in was {n}, and the time was {total_time}. So, I could go 7 higher.")

    # How much higher can you go (approximately) on List 3 with 2^n before the function takes 3 seconds to run?
    n = 24
    total_time = time_the_function(2, n)
    print(f"The number I plugged in was {n}, and the time was {total_time}. So, I could go 4 higher.")
    
    print()


if __name__ == "__main__":
    main()