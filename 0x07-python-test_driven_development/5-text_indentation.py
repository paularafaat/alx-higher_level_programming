#!/usr/bin/python3
"""module for text indentation"""


def text_indentation(text):
    """text indentation

    Args:
        text (str):

    Raises:
        TypeError: _if the text was not string_
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for delim in ".?:":
        lines = []
        for line in text.split(delim):
            lines.append(line.strip(" "))
        text = (delim + "\n\n").join(lines)
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
