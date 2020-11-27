# Taken from https://gist.github.com/j6k4m8/24f028250dc38eb8579e4b9090beeeb6


class Colors:
    """
    A "color-scheme" with default formatting options.

    Useful for writing user-facing output to TTY terminals.

    """

    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


class NoColors:
    """
    A "color-scheme" with no formatting options.

    Useful for writing to non-TTY terminals.

    """

    PURPLE = ""
    CYAN = ""
    DARKCYAN = ""
    BLUE = ""
    GREEN = ""
    YELLOW = ""
    RED = ""
    BOLD = ""
    UNDERLINE = ""
    END = ""


def pretty_print(colors, text, cr=True):
    """
    Print a string with CLI color and formatting options.

    Arguments:
        colors (list): A list of color formatting options
        text (str): The string to format
        cr (bool: True): Whether to include a carriage return.

    Returns:
        None

    """
    if isinstance(colors, list):
        pre = "".join(colors)
    else:
        pre = colors

    if cr:
        print(pre + text + Colors.END)
    else:
        print(pre + text + Colors.END, end="")


def pretty_format(colors, text):
    """
    Format a string with CLI color and formatting options.

    Arguments:
        colors (list): A list of color formatting options
        text (str): The string to format

    Returns:
        str: The formatted string

    """
    if isinstance(colors, list):
        pre = "".join(colors)
    else:
        pre = colors

    return pre + text + Colors.END
