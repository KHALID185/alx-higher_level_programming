#!/usr/bin/python3
"""a module to return into the new line if we have (. ? :)"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after (.,?,:)

    args:
    text: a string

    raises:
    TypeError if text is not a string

    return:
    void
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for dlm in ".?:":
        text = (dlm + "\n\n").join(
                [rw.strip(" ") for rw in text.split(dlm)])
    print(text, end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
