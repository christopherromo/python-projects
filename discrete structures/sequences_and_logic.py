"""
sequences_and_logic.py

Exercises involving sequences and propositional logic.

Author: Christopher Romo
"""


def closed_pie(n: int) -> float:
    """
    Returns the maximum number of pieces we could get with n cuts.

    Args:
        n (int): The number of cuts.
    
    Returns:
        float: The maximum number of pieces.
    """

    pie_pieces = ((n ** 2) + n + 2) / 2
    return pie_pieces


def recursive_pie(n: int) -> float:
    """
    Returns the maximum number of pieces we could get with n cuts using recursion.

    Args:
        n (int): The number of cuts.

    Returns:
        float: The maximum number of pieces.
    """

    if n == 1:
        return 2
    else:
        return recursive_pie(n - 1) + n


def a_wild_function_appears(p: bool, q: bool, r: bool, s: bool) -> bool:
    """
    Analyzes the given propositional logic.

    Args:
        p (bool): Proposition p.
        q (bool): Proposition q.
        r (bool): Proposition r.
        s (bool): Proposition s.

    Returns:
        bool: The result of the logical analysis.
    """

    if not s and not r:
        if p and r:
            return True
        if p:
            return True
        if q and r:
            return True
        if q:
            return True
        return False
    return False


def a_calm_function_emerges(p: bool, q: bool, r: bool, s: bool) -> bool:
    """
    Analyzes the given propositional logic.

    Args:
        p (bool): Proposition p.
        q (bool): Proposition q.
        r (bool): Proposition r.
        s (bool): Proposition s.

    Returns:
        bool: The result of the logical analysis.
    """

    if not (s or r):
        if r:
            if p or q:
                return True
        if p or q:
            return True
        return False
    return False


def main() -> None:
    """Program entry point."""

    # originally a jupyter notebook exercise
    
    # task 1

    # Your task is to define a Python function closed_pie(n) that returns the
    # maximum number of pieces we could get with n cuts. Note that the provided
    # print statement should output the first 15 elements of the sequence once
    # you complete the body of the function.

    print("task 1 output:")
    print([closed_pie(x) for x in range(1,16)])
    
    # task 2

    # Your task is to define a Python function recursive_pie(n) based on this
    # formula that returns the maximum number of pieces we could get with n cuts.
    # Note that this function should be recursive; that is it should call itself
    # in the process of obtaining the answer. Again a print statement is provided
    # that will print the first 15 elements of the sequence.

    print("\ntask 2 output:")
    print([recursive_pie(x) for x in range(1,16)])

    # task 3

    # Your task is to analyze the following function (a_wild_function_appears)
    # and provide a propositional statement that matches its logic.

    # (-s and -r) and ((p and r) or (p) or (q and r) or (q))

    # task 4

    # Your final task is to use the logical equivalences given in Theorem 2
    # from the book to simplify the statement from Deliverable \#3, and then
    # provide a new, simpler, and equivalent function (a_calm_function_emerges).

    # -(s or r) and ((r and (p or q)) or (p or q))


if __name__ == "__main__":
    main()