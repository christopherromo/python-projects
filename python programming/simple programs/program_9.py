"""
program_9.py

Mathplotlib example (sin wave).

Author: Christopher Romo
"""

import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    """Program entry point."""

    # from in-class example

    # generate x values from 0 to 2 pi
    x_values = np.linspace(0, 2 * np.pi)

    # plot sine waves with different frequencies
    for i in range(1, 4):
        y_values = np.sin(x_values * i)
        plt.plot(x_values, y_values)

    # display the plot
    plt.show()


if __name__ == "__main__":
    main()
