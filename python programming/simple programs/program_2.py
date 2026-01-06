"""
program_2.py

Object and class example.

Author: Christopher Romo
"""


class Car:
    """A simple Car class."""

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return f"The {self.color} car has {self.mileage} miles."


def main() -> None:
    """Program entry point."""

    # demonstration of the Car class
    car_one = Car('blue', 20000)
    car_two = Car('red', 30000)

    print(car_one)
    print(car_two)


if __name__ == "__main__":
    main()