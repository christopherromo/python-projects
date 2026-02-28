"""
program_1.py

printing and dictionary example.

author: christopher romo
"""


def print_picnic(items_dict: dict, left_width: int, right_width: int) -> None:
    """
    prints a formatted picnic items list.

    args:
        items_dict (dict): a dictionary of picnic items and their quantities.
        left_width (int): the width for the left column.
        right_width (int): the width for the right column.
    """

    print("PICNIC ITEMS".center(left_width + right_width, "-"))

    # print each item with formatting
    for key, value in items_dict.items():
        print(key.ljust(left_width, ".") + str(value).rjust(right_width))


def main() -> None:
    """printing and dictionary example."""

    # printing examples
    print("hello")
    print("Hello".rjust(20, "*"))

    # dictionary example
    picnic_items = {"sandwiches": 4, "apples": 12, "cups": 4, "cookies": 8000}

    # print picnic items with different widths
    print_picnic(picnic_items, 12, 5)
    print_picnic(picnic_items, 20, 6)


if __name__ == "__main__":
    main()
