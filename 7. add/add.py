
def add(*args):
    """Adding to matrices!

    This function takes two matrices of the same size and performs matrix
    addition.

    Args:
        mtx_one: a matrix of integers
        mtx_two: anoter matrix of integers

    Returns:
        A matrix containing the added values
    """
    
    rows = len(args[0])
    cols = len(args[0][0])

    # checking size for all matrices
    for arg in args:
        # checking the rows of each matrix
        if len(arg) != rows:
            raise ValueError("Given matrices are not the same size.")
        # checking the columns
        for col in arg:
            if len(col) != cols:
                raise ValueError("Given matrices are not the same size.")

    final_matrix = shallow_copy(args[0], rows, cols)
    
    # for each row
    for row in range(rows):
        # for each column
        for col in range(cols):
            # for each matrix
            for i in range(1, len(args)):
                # add the values into the first matrix
                final_matrix[row][col]+= args[i][row][col]

    return final_matrix

def shallow_copy(to_copy, rows, cols):
    """Need i say?
    """
    clean_mtx = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(to_copy[i][j])
        clean_mtx.append(row)
    return clean_mtx


