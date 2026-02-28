"""
program_4.py

iterator example.

author: christopher romo
"""


class MultipleOfFive:
    """an iterator that yields multiples of five within a specified range."""

    def __init__(self, minimum: int, maximum: int) -> None:
        for value in range(minimum, maximum):
            if value % 5 == 0:
                break
        self.minimum = value
        self.maximum = maximum

    def __iter__(self) -> "MultipleOfFive":
        return self

    def __next__(self) -> int:
        if self.minimum < self.maximum:
            value = self.minimum
            self.minimum += 5
            return value
        else:
            raise StopIteration()


def main() -> None:
    """iterator example."""

    # demonstration of the MultipleOfFive iterator
    the_list = MultipleOfFive(1, 51)

    # print the multiples of five
    for element in the_list:
        print(element)


if __name__ == "__main__":
    main()
