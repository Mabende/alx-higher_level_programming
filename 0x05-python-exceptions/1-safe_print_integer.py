#!/usr/bin/python3


def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value: the value to be printed.

    Returns:
        true if printing is successful, False otherwise
        """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)


