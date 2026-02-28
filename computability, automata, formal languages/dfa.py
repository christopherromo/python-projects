"""
dfa.py

implements a deterministic finite automaton (dfa) that reads its configuration
from a file.

author: christopher romo
created: 2025-03-14
"""


def next_state(current_state: int, input: str, alphabet: list, states: list) -> int:
    """
    determines the next state based on the current state and input character.

    args:
        current_state (int): the current state as an integer.
        input (str): the current input character.
        alphabet (list): the list of characters in the dfa's alphabet.
        states (list): the list of state transitions.

    returns:
        int: the next state as an integer.
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
    """reads the dfa configuration from a file and runs the dfa on user input."""

    # input file format:
    # line 1: alphabet (string of characters)
    # line 2: number of states (integer)
    # next n lines: state transitions (space-separated integers for each state)
    # last line: accept states (space-separated integers)

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
