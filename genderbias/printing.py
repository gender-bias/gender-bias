# Taken from https://gist.github.com/j6k4m8/24f028250dc38eb8579e4b9090beeeb6


class Colors:
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
    if isinstance(colors, list):
        pre = "".join(colors)
    else:
        pre = colors

    if cr:
        print(pre + text + Colors.END)
    else:
        print(pre + text + Colors.END, end="")


def pretty_format(colors, text):
    if isinstance(colors, list):
        pre = "".join(colors)
    else:
        pre = colors

    return pre + text + Colors.END
