"""
branch_predictor.py

Implements various branch predictors including one-bit, two-bit, and n-bit
predictors.

Author: Christopher Romo
Created: 2024-10-13
"""

from random import paretovariate
from random import random


def next_branch_outcome_loop() -> bool:
    """
    Generates the next branch outcome in a looping pattern.

    Returns:
        bool: The next branch outcome (True for taken, False for not taken).
    """

    alpha = 2
    outcome = paretovariate(alpha)
    outcome = outcome > 2
    return outcome


def next_branch_outcome_random() -> bool:
    """
    Generates the next branch outcome randomly.

    Returns:
        bool: The next branch outcome (True for taken, False for not taken).
    """

    outcome = random()
    outcome = outcome > 0.5
    return outcome


class Predictor:
    """A base class for branch predictors."""

    def __init__(self):
        self.state = 0

    def next_predict(self):
        """
        Use this method to return the prediction based off of the current
        state.
        """

    def incorrect_predict(self):
        """
        Use this method to set the next state if an incorrect predict
        occurred. (self.state = next_state)
        """

    def correct_predict(self):
        """
        Use this method to set the next state if an incorrect predict
        occurred. (self.state = next_state)
        """


class OneBitPredictor(Predictor):
    """A one-bit branch predictor."""

    def next_predict(self) -> int:
        """
        If the state is 0, predict not taken (0). If the state is 1, predict
        taken (1).

        Returns:
            int: The predicted branch outcome (0 for not taken, 1 for taken).
        """

        if self.state == 0:
            return 0
        else:
            return 1

    def incorrect_predict(self) -> None:
        """Updates the current state opposite the prediction."""

        if self.state == 0:
            self.state = 1
        else:
            self.state = 0

    def correct_predict(self) -> None:
        """Updates the current state based on the prediction."""

        if self.state == 0:
            self.state = 0
        else:
            self.state = 1


class TwoBitPredictor(Predictor):
    """A two-bit branch predictor."""

    def next_predict(self) -> int:
        """
        If the state is 0 or 1, predict not taken (0). If the state is 2 or 3,
        predict taken (1).

        Returns:
            int: The predicted branch outcome (0 for not taken, 1 for taken).
        """

        if self.state == 0:
            return 0
        elif self.state == 1:
            return 0
        elif self.state == 2:
            return 1
        else:
            return 1

    def incorrect_predict(self) -> None:
        """Updates the current state opposite the prediction."""

        if self.state == 0:
            self.state = 1
        elif self.state == 1:
            self.state = 2
        elif self.state == 2:
            self.state = 1
        else:
            self.state = 2

    def correct_predict(self) -> None:
        """Updates the current state based on the prediction."""

        if self.state == 0:
            self.state = 0
        elif self.state == 1:
            self.state = 0
        elif self.state == 2:
            self.state = 3
        else:
            self.state = 3


class NBitPredictor(Predictor):
    """An n-bit branch predictor."""

    def __init__(self, n_bits):
        self.n_bits = n_bits
        self.state = 0

    def next_predict(self) -> int:
        """
        Predicts the next branch outcome based on the current state.

        Returns:
            int: The predicted branch outcome (0 for not taken, 1 for taken).
        """

        # get the total number of nodes and find the halfway point
        node_num = 2**self.n_bits
        half_point = node_num // 2

        # create predictions, if below half, predict 0, if above, predict 1
        if self.state <= half_point:
            return 0
        else:
            return 1

    def incorrect_predict(self) -> None:
        """Updates the current state opposite the prediction."""

        node_num = 2**self.n_bits
        half_point = node_num // 2

        if self.state <= half_point:
            self.state = self.state + 1
        else:
            self.state = self.state - 1

    def correct_predict(self) -> None:
        """Updates the current state based on the prediction."""

        node_num = 2**self.n_bits
        half_point = node_num // 2

        if self.state <= half_point:
            if self.state == 0:
                self.state = 0
            else:
                self.state = self.state - 1
        else:
            if self.state == node_num:
                self.state = node_num
            else:
                self.state = self.state + 1


def main() -> None:
    """Program entry point."""

    # originally a jupyter notebook exercise

    # task 1

    # Complete the OneBitPredictor class by implementing the next_predict,
    # incorrect_predict, and correct_predict methods. This instantiation will
    # be used to compute the prediction accuracy. Use the next_predict method
    # of the class to predict the next branch state. If the predict is
    # incorrect, use the incorrect_predict method to set the next state. If
    # the predict is correct, use the correct_predict method to set the next
    # state.

    # task 2

    # Use the next_branch_outcome_random method to generate branch outcomes.
    # Use the previously implemented methods to compute a prediction rate.

    # create a branch predictor object and start a counter
    branch_predictor = OneBitPredictor()
    correct_count = 0

    for i in range(0, 25):
        # make prediction and get actual outcome
        next_branch_prediction = branch_predictor.next_predict()
        next_branch_outcome = next_branch_outcome_random()

        # if they are equal, increment the counter and set the state for a
        # correct prediction
        if next_branch_prediction == next_branch_outcome:
            correct_count += 1
            branch_predictor.correct_predict()
        else:
            # set the state for an incorrect prediction
            branch_predictor.incorrect_predict()

    # get the correct rate and print
    prediction_rate = correct_count / 25
    print("OneBitPredictor, next_branch_outcome_random")
    print(prediction_rate)
    print()

    # task 3

    # Use the next_branch_outcome_loop method to generate branch outcomes.
    # Use the previously implemented methods to compute a prediction rate.

    # create a branch predictor object and start a counter
    branch_predictor = OneBitPredictor()
    correct_count = 0

    for i in range(0, 25):
        # make prediction and get actual outcome
        next_branch_prediction = branch_predictor.next_predict()
        next_branch_outcome = next_branch_outcome_loop()

        # if they are equal, increment the counter and set the state for a
        # correct prediction
        if next_branch_prediction == next_branch_outcome:
            correct_count += 1
            branch_predictor.correct_predict()
        else:
            # set the state for an incorrect prediction
            branch_predictor.incorrect_predict()

    # get the correct rate and print
    prediction_rate = correct_count / 25
    print("OneBitPredictor, next_branch_outcome_loop")
    print(prediction_rate)
    print()

    # task 4

    # Complete the TwoBitPredictor class by implementing the next_predict,
    # incorrect_predict, and correct_predict methods. This instantiation will
    # be used to compute the prediction accuracy. Use the next_predict method
    # of the class to predict the next branch state. If the predict is
    # incorrect, use the incorrect_predict method to set the next state. If the
    # predict is correct, use the correct_predict method to set the next state.

    # task 5

    # Use the next_branch_outcome_random method to generate branch outcomes.
    # Use the previously implemented methods to compute a prediction rate.

    # create a branch predictor object and start a counter
    branch_predictor = TwoBitPredictor()
    correct_count = 0

    for i in range(0, 25):
        # make prediction
        next_branch_prediction = branch_predictor.next_predict()

        # if the prediction is above half, predict 1
        if next_branch_prediction == 2 or next_branch_prediction == 3:
            next_branch_prediction = 1
        else:
            # predict 0
            next_branch_prediction = 0

        # get actual outcome
        next_branch_outcome = next_branch_outcome_random()

        # if they are equal, increment the counter and set the state for a
        # correct prediction
        if next_branch_prediction == next_branch_outcome:
            correct_count += 1
            branch_predictor.correct_predict()
        else:
            # set the state for an incorrect prediction
            branch_predictor.incorrect_predict()

    # get the correct rate and print
    prediction_rate = correct_count / 25
    print("TwoBitPredictor, next_branch_outcome_random")
    print(prediction_rate)
    print()

    # task 6

    # Use the next_branch_outcome_loop method to generate branch outcomes. Use
    # the previously implemented methods to compute a prediction rate.

    # create a branch predictor object and start a counter
    branch_predictor = TwoBitPredictor()
    correct_count = 0

    for i in range(0, 25):
        # make prediction
        next_branch_prediction = branch_predictor.next_predict()

        # if the prediction is above half, predict 1
        if next_branch_prediction == 2 or next_branch_prediction == 3:
            next_branch_prediction = 1
        else:
            # predict 0
            next_branch_prediction = 0

        # get actual outcome
        next_branch_outcome = next_branch_outcome_loop()

        # if they are equal, increment the counter and set the state for a
        # correct prediction
        if next_branch_prediction == next_branch_outcome:
            correct_count += 1
            branch_predictor.correct_predict()
        else:
            # set the state for an incorrect prediction
            branch_predictor.incorrect_predict()

    # get the correct rate and print
    prediction_rate = correct_count / 25
    print("TwoBitPredictor, next_branch_outcome_loop")
    print(prediction_rate)
    print()

    # task 7

    # Inherit the Predictor class and implement it's methods just like before.
    # Now, implement an n-bit predictor that represents a higher confidence
    # prediction.

    # task 8

    # Use the `next_branch_outcome_random` method to generate branch outcomes.
    # Use the previously implemented methods to compute a prediction rate.

    # create a branch predictor object and start a counter
    n_bits = 3
    branch_predictor = NBitPredictor(n_bits)
    correct_count = 0

    for i in range(0, 25):
        # initiate variables
        node_num = 2**n_bits
        half_point = node_num // 2

        # make prediction
        next_branch_prediction = branch_predictor.next_predict()

        # if the prediction is above half, predict 1
        if next_branch_prediction > half_point:
            next_branch_prediction = 1
        else:
            # predict 0
            next_branch_prediction = 0

        # get actual outcome
        next_branch_outcome = next_branch_outcome_random()

        # if they are equal, increment the counter and set the state for a
        # correct prediction
        if next_branch_prediction == next_branch_outcome:
            correct_count += 1
            branch_predictor.correct_predict()
        else:
            # set the state for an incorrect prediction
            branch_predictor.incorrect_predict()

    # get the correct rate and print
    prediction_rate = correct_count / 25
    print("NBitPredictor, next_branch_outcome_random")
    print(prediction_rate)
    print()

    # task 9

    # Use the next_branch_outcome_loop method to generate branch outcomes. Use
    # the previously implemented methods to compute a prediction rate.

    # create a branch predictor object and start a counter
    n_bits = 3
    branch_predictor = NBitPredictor(n_bits)
    correct_count = 0

    for i in range(0, 25):
        # initiate variables
        node_num = 2**n_bits
        half_point = node_num // 2

        # make prediction
        next_branch_prediction = branch_predictor.next_predict()

        # if the prediction is above half, predict 1
        if next_branch_prediction > half_point:
            next_branch_prediction = 1
        else:
            # predict 0
            next_branch_prediction = 0

        # get actual outcome
        next_branch_outcome = next_branch_outcome_loop()

        # if they are equal, increment the counter and set the state for a
        # correct prediction
        if next_branch_prediction == next_branch_outcome:
            correct_count += 1
            branch_predictor.correct_predict()
        else:
            # set the state for an incorrect prediction
            branch_predictor.incorrect_predict()

    # get the correct rate and print
    prediction_rate = correct_count / 25
    print("NBitPredictor, next_branch_outcome_loop")
    print(prediction_rate)


if __name__ == "__main__":
    main()
