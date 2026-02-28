"""
program_3.py

inheritance and default parameter example.

author: christopher romo
"""


class Dog:
    """the Dog class creates a dog object."""

    species = "Canis familiaris"

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def speak(self, sound: str) -> str:
        """
        returns a string representing the sound the dog makes.

        args:
            sound (str): the sound the dog makes.

        returns:
            str: a string in the format "<name> says <sound>."
        """

        return f"{self.name} says {sound}."

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."


class GoldenRetriever(Dog):
    """the GoldenRetriever class creates a golden retriever dog object."""

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    def speak(self, sound: str = "Bark") -> str:
        """
        returns a string representing the sound the golden retriever makes.

        args:
            sound (str): the sound the golden retriever makes (default is
            "Bark").

        returns:
            str: a string in the format "<name> says <sound>."
        """

        return f"{self.name} says {sound}."


def main() -> None:
    """inheritance and default parameter example."""

    # demonstration of the Dog and GoldenRetriever classes
    max = GoldenRetriever("Max", 9)

    # print details and sounds
    print(max.speak())
    print(max.speak("Hello"))
    print(max.__str__())


if __name__ == "__main__":
    main()
