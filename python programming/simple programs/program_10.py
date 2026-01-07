"""
program_10.py

Mathplotlib example (scatter plot).

Author: Christopher Romo
"""


import numpy as np
import matplotlib.pyplot as plt


def main() -> None:
    """Program entry point."""

    n = 1500

    # generate random x and y values between -1 and 1
    x_values = np.random.rand(n, 2) * 2 - 1
    points_color = np.ones(n)

    # determine colors based on quadrants
    set1 = np.where(x_values[:,0] >= 0)
    set2 = np.where(x_values[:,1] >= 0)
    points_color[np.intersect1d(set1, set2)] = 0

    set1 = np.where(x_values[:,0] < 0)
    set2 = np.where(x_values[:,1] < 0)
    points_color[np.intersect1d(set1, set2)] = 0

    # plot the scatter plot
    plt.scatter(x_values[:,0], x_values[:,1], c = points_color)
    plt.show()


if __name__ == "__main__":
    main()