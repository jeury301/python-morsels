def matrix_from_string(mtx_str):
    """Turning a string into it's matrix representation.

    This function accepts a string representation of a matrix, and turns it
    into an actual matrix. This function uses \n as a delimiter for the rows,
    and ignores any extra spaces.

    Turned into a one-liner comprehension, it's equivalent was commented out.

    Args:
        mtx_str: A string representation of a matrix

    Returns:
        An actual matrix for the string
    """

    # mtx_rows = mtx_str.split("\n")
    # final_matrix = []
    #
    # for row in mtx_rows:
    #     if row.replace(" ", "") != "":
    #         mtx_row = [float(col) for col in row.strip().split(" ") if col != ""]
    #         final_matrix.append(mtx_row)
    # return final_matrix
    return ([[float(col) for col in row.strip().split(" ") if col != ""]
        for row in mtx_str.split("\n") if row.replace(" ", "") != ""])
