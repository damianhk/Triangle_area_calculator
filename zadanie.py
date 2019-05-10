import sys
from math import sqrt


def read_data():
    """
    Return readed data from standard input,
    splited with space separator,
    converted to list of float numbers

    Input:
    - data from file input
      example: $ python scrpit.py < file.txt
    - data from sys.stdin in program
      example:
      # put this in your script
      import io, sys
      sys.stdin = io.StringIO('string type data')

    Output:
    - list with float numbers
    """
    # Check if data is passed into standard input
    if not sys.stdin.isatty():
        # Check if data is not empty
        if sys.stdin.readline() == '':
            raise ValueError('File is empty')

        # Set current positon on beginning
        sys.stdin.seek(0)

        lines = sys.stdin.readline()
        lines = lines.split(' ')
        lines = [float(element) for element in lines]
        return lines
    else:
        raise ValueError('No file is passed into standart input')


def trianagle_area(sides):
    """
    Return triangle size from only sides.

    Input:
    - List, touple, set with 3 non-negative real number

    Output:
    - Size rounded to two decimals places
    """
    # Check input type
    if not isinstance(sides, (list, tuple, set)):
        raise TypeError(
            "Input value must be a list with 3 items, not {}".format(
                type(sides)))
    elif len(sides) != 3:
        raise ValueError("Input must be a 3 items list, not {}".format(len(sides)))

    # Check if input values are positive real numbers
    for item in sides:
        if not isinstance(item, (int, float)) or isinstance(item, bool):
            raise TypeError("The side must be a non-negative real number, not {}".format(type(item)))
        if item <= 0:
            raise ValueError("The side have to be a positive real numbers.")

    # Compute size from Heron's formula. Check if from sides can we build triangles
    p = 1 / 2 * (sum(sides))
    x = p
    for item in sides:
        x *= p - item
    if x <= 0:
        raise ValueError("From this sides cannot build trianagle.")
    S = sqrt(x)

    # Return size rounded to two decimal places
    return round(S, 2)


if __name__ == '__main__':
    sides = read_data()
    print(trianagle_area(sides))
