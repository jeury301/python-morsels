def v0_matrix_from_string(matrix_string):
    """Convert string-based rows of numbers to list of lists.

    Splitting our matrix string by newline characters to get rows, splitting
    the rows by consecutive whitespace characters to get the elements, and
    converting each element to a float to populate our matrix with.
    We're populating our matrix by making an empty row for each line and
    filling it with numbers and then putting that row in our new matrix list.
    """
    matrix = []
    for row_string in matrix_string.split('\n'):
        row = []
        for n in row_string.split():
            row.append(float(n))
        matrix.append(row)
    return matrix

def v1_matrix_from_string(matrix_string):
    """Convert string-based rows of numbers to list of lists.

    Fixing the error on the previous solution with the extra line at the endself.
    Using - splitlines - which does the same thing as .split("\n") but removes
    the trailing line.
    """
    matrix = []
    for row_string in matrix_string.splitlines():
        row = []
        for n in row_string.split():
            row.append(float(n))
        matrix.append(row)
    return matrix

def v2_matrix_from_string(matrix_string):
    """Convert string-based rows of numbers to list of lists.

    Turning inner - row - for loop into a list comprehension.
    """
    matrix = []
    for row_string in matrix_string.splitlines():
        matrix.append([float(n) for n in row_string.split()])
    return matrix

def v3_matrix_from_string(matrix_string):
    """Convert string-based rows of numbers to list of lists.

    Turning everything into a list comprehension
    """
    return [
        [float(n) for n in row_string.split()]
        for row_string in matrix_string.splitlines()
    ]
    
def v4_matrix_from_string(matrix_string):
    """Convert string-based rows of numbers to list of lists.

    Solving bonus 1 - code to work even if there were empty/blank lines in the
    middle of the file, or even for lines that contained
    nothing but whitespace characters - for this we add a condition to check if
    the line is not empty.
    """
    return [
        [float(n) for n in row_string.split()]
        for row_string in matrix_string.splitlines()
        if row_string.strip()
    ]
