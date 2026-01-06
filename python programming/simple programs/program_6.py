"""
program_6.py

Datetime and time example.

Author: Christopher Romo
"""


import datetime, time


def main() -> None:
    """Program entry point."""

    the_date = datetime.datetime(2026, 1, 5, 0, 0, 0)

    # wait until the specified date (Midnight, January 5, 2026)
    while datetime.datetime.now() < the_date:
        time.sleep(10)

    print('Done')


if __name__ == "__main__":
    main()