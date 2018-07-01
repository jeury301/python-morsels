def v0_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices.

    Very inneficient not pythonic-like solution using indices.
    """
    combined = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[i])):
            row.append(matrix1[i][j] + matrix2[i][j])
        combined.append(row)
    return combined


def v1_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices.

    Using the zip function to iterate over the 2 matrices at the same time.
    """
    combined = []
    for rows in zip(matrix1, matrix2):
        row = []
        for items in zip(rows[0], rows[1]):
            row.append(items[0] + items[1])
        combined.append(row)
    return combined

def v2_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices.

    Making the previous solution more readable by using multiple assignments,
    instead of hard-coded indices.
    """
    combined = []
    for row1, row2 in zip(matrix1, matrix2):
        row = []
        for n, m in zip(row1, row2):
            row.append(n + m)
        combined.append(row)
    return combined

def v3_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices.

    Using a very fancy list comprehension to replace the creation of the
    empty list - row = [].
    """
    combined = []
    for row1, row2 in zip(matrix1, matrix2):
        row = [
            n + m
            for n, m in zip(row1, row2)
        ]
        combined.append(row)
    return combined

def v4_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices.

    Removing the variable - row - altogether.
    """
    combined = []
    for row1, row2 in zip(matrix1, matrix2):
        combined.append([
            n + m
            for n, m in zip(row1, row2)
        ])
    return combined

def v5_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices.

    Writing the list comprehension as a one-liner
    """
    combined = []
    for row1, row2 in zip(matrix1, matrix2):
        combined.append([n + m for n, m in zip(row1, row2)])
    return combined

def v6_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices.

    Turning the outer loop into a list-comprehension.
    """
    return [
        [n + m for n, m in zip(row1, row2)]
        for row1, row2 in zip(matrix1, matrix2)
    ]

def v7_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices.

    One-liner solution =}
    """
    return [[n+m for n, m in zip(r1, r2)] for r1, r2 in zip(matrix1, matrix2)]

def v8_add(*matrices):
    """Add corresponding numbers in given 2-D matrices.

    Solving the first bonus - accepting any number of matrices
    """
    combined = []
    for rows in zip(*matrices):
        row = []
        for values in zip(*rows):
            total = 0
            for n in values:
                total += n
            row.append(total)
        combined.append(row)
    return combined

def v9_add(*matrices):
    """Add corresponding numbers in given 2-D matrices.

    Using the - sum - function so sum over the row values.
    """
    combined = []
    for rows in zip(*matrices):
        row = []
        for values in zip(*rows):
            row.append(sum(values))
        combined.append(row)
    return combined

def v10_add(*matrices):
    """Add corresponding numbers in given 2-D matrices.

    Turning previous solution into a one-liner list comprehension.
    """
    return [[sum(values) for values in zip(*rows)] for rows in zip(*matrices)]

def v11_add(matrix1, matrix2):
    """Add corresponding numbers in given 2-D matrices.

    Solving the second bonus - raise a ValueError exception when our
    lists-of-lists were different shapes.

    Calculating the length of the matrices to determine
    if they are the same size.
    """
    if [len(r) for r in matrix1] != [len(r) for r in matrix2]:
        raise ValueError("Given matrices are not the same size.")
    return [
        [n + m for n, m in zip(row1, row2)]
        for row1, row2 in zip(matrix1, matrix2)
    ]

def v12_add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    matrix_shapes = {
        tuple(len(r) for r in matrix)
        for matrix in matrices
    }
    if len(set(matrix_shapes)) > 1:
        raise ValueError("Given matrices are not the same size.")
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]

def v13_add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    try:
        from itertools import zip_longest
        return [
            [sum(values) for values in zip_longest(*rows)]
            for rows in zip_longest(*matrices)
        ]
    except TypeError as e:
        raise ValueError("Given matrices are not the same size.") from e

def get_shape(matrix):
    return [len(r) for r in matrix]

def v14_add(*matrices):
    """Add corresponding numbers in given 2-D matrices."""
    shape_of_matrix = get_shape(matrices[0])
    if any(get_shape(m) != shape_of_matrix for m in matrices):
        raise ValueError("Given matrices are not the same size.")
    return [
        [sum(values) for values in zip(*rows)]
        for rows in zip(*matrices)
    ]
