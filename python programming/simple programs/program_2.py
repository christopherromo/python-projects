"""
program_2.py

object and class example.

author: christopher romo
"""


class Car:
    """the Car class creates a car object."""

    def __init__(self, color: str, mileage: int) -> None:
        self.color = color
        self.mileage = mileage

    def __str__(self) -> str:
        return f"The {self.color} car has {self.mileage} miles."


def main() -> None:
    """object and class example."""

    # demonstration of the Car class
    car_one = Car("blue", 20000)
    car_two = Car("red", 30000)

    # print the car details
    print(car_one)
    print(car_two)


if __name__ == "__main__":
    main()
