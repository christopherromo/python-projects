"""
program_3.py

Inheritance and default parameter example.

Author: Christopher Romo
"""


class Dog:
    """A simple Dog class."""

    species = "Canis familiaris"

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def speak(self, sound: str) -> str:
        """
        Returns a string representing the sound the dog makes.
        
        Args:
            sound: The sound the dog makes.

        Returns:
            A string in the format "<name> says <sound>."
        """

        return f"{self.name} says {sound}."

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old."


class GoldenRetriever(Dog):
    """A Golden Retriever class that inherits from Dog."""

    def __init__(self, name: str, age: int) -> None:
        super().__init__(name, age)

    def speak(self, sound: str = "Bark") -> str:
        """
        Returns a string representing the sound the golden retriever makes.
        
        Args:
            sound: The sound the golden retriever makes (default is "Bark").
        
        Returns:
            A string in the format "<name> says <sound>."
        """

        return f"{self.name} says {sound}."


def main() -> None:
    """Program entry point."""

    # demonstration of the Dog and GoldenRetriever classes
    max = GoldenRetriever('Max', 9)
    
    # print details and sounds
    print(max.speak())
    print(max.speak("Hello"))
    print(max.__str__())


if __name__ == "__main__":
    main()