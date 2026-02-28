"""
program_6.py

datetime and time example.

author: christopher romo
"""

import datetime, time


def main() -> None:
    """datetime and time example."""

    the_date = datetime.datetime(2026, 1, 5, 0, 0, 0)

    # wait until the specified date (midnight, January 5, 2026)
    while datetime.datetime.now() < the_date:
        time.sleep(10)

    # print message when the date is reached
    print("Done.")


if __name__ == "__main__":
    main()
