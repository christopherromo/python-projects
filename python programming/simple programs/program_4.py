"""
program_4.py

Iterator example.

Author: Christopher Romo
"""


class MultipleOfFive:
    """An iterator that yields multiples of five within a specified range."""

    def __init__(self, minimum, maximum):
        for value in range(minimum, maximum):
            if value % 5 == 0:
                break
        self.minimum = value
        self.maximum = maximum

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.minimum < self.maximum:
            value = self.minimum
            self.minimum += 5
            return value
        else:
            raise StopIteration()


def main() -> None:
    """Program entry point."""

    # demonstration of the MultipleOfFive iterator
    the_list = MultipleOfFive(1,51)

    for element in the_list:
        print(element)


if __name__ == "__main__":
    main()