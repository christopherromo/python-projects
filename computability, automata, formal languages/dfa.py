"""
dfa.py

Implements a deterministic finite automaton (DFA) that reads its configuration 
from a file.

Author: Christopher Romo
Created: 2025-03-14
"""


def next_state(current_state: int, input: str, alphabet: list, states: list) -> int:
    """
    Determines the next state based on the current state and input character.

    Args:
        current_state (int): The current state as an integer.
        input (str): The current input character.
        alphabet (list): The list of characters in the DFA's alphabet.
        states (list): The list of state transitions.

    Returns:
        int: The next state as an integer.
    """

    # find the x position in states list
    counter = 0
    next_state_pos = 0

    for i in range(0, len(alphabet)):
        if alphabet[i] == input:
            next_state_pos = counter
        else:
            counter += 1

    # return the int of the next states position in current state list
    return int(states[current_state][next_state_pos])


def main() -> None:
    """Program entry point."""

    # Input file format:
    # Line 1: Alphabet (string of characters)
    # Line 2: Number of states (integer)
    # Next N Lines: State transitions (space-separated integers for each state)
    # Last Line: Accept states (space-separated integers)

    input_file = open("dfa_states1_input.txt", "r")

    # read the alphabet
    alphabet_string = input_file.readline()
    alphabet = list(alphabet_string[:-1])

    # read the number of states
    num_states = int(input_file.readline())

    # read all of the states
    states = list()
    for i in range(0, num_states):
        state = input_file.readline()
        state = state.split()
        states.append(state)

    # read the accept states
    accept_states = input_file.readline()
    accept_states = accept_states.split()

    # ensure all states are processed as ints
    for i in range(0, len(accept_states)):
        accept_states[i] = int(accept_states[i])

    # prompt for input
    the_string = input("Please enter a string, to exit enter 'exit': ")

    while the_string != "exit":
        # reset the current state
        current_state = 0

        # iterate through string
        for i in range(0, len(the_string)):
            print(
                "Current State: "
                + str(current_state)
                + ", Current Input Character: "
                + the_string[i]
            )

            # check the current character and ensure it is in alphabet
            if the_string[i] not in alphabet:
                print("Symbol not in alphabet!")
                current_state = -1
                break

            # update current state based on input character
            current_state = next_state(current_state, the_string[i], alphabet, states)
            print("Moving to State " + str(current_state))

        # check to see if current state is in accept list
        if current_state in accept_states:
            print("The string was accepted.")
        else:
            print("The string was rejected.")

        # prompt for next string
        the_string = input("Please enter a string, to exit enter 'exit': ")

    # close out program
    print("Exited successfully!")
    input_file.close()


if __name__ == "__main__":
    main()
