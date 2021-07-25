from itertools import product


def saddle_points(matrix: list) -> list:
    """
    Estimate and return number of saddle points in a matrix.
    """

    # Check if matrix is empty, in that case return an empty matrix accoirding
    # to specification.
    if matrix == []:
        return []

    # Create a list (set) of unique lengths of respective row in the matrix. If
    # the returning list has more unique values than one. Then the matrix is
    # deemed to be irregular.
    if len(set([len(row) for row in matrix])) > 1:
        raise ValueError("Matrix is irregular")

    rows = range(1, len(matrix) + 1)
    cols = range(1, len(matrix[0]) + 1)

    # Insert all combinations of row numbers and col numbers into a list.
    rows_and_cols = list(product(rows, cols))
    saddle_point = []

    # Loop through all rows and cols
    for row_nr, col_nr in rows_and_cols:
        # Check whether current location (number) is a saddle point
        number = matrix_item(row_nr, col_nr, matrix)
        if number >= max(row(row_nr, matrix)) and number <= min(
                column(col_nr, matrix)):
            saddle_point.append({"row": row_nr, "column": col_nr})

    return saddle_point


def matrix_item(row_nr: int, col_nr: int, matrix: list) -> int:
    """
    Return item at location (row_nr, col_nr).
    """
    return row(row_nr, matrix)[col_nr - 1]


def row(row: int, matrix: list) -> list[int]:
    """
    Return certain row of a matrix.
    """
    return matrix[row - 1]


def column(column: int, matrix: list) -> list[int]:
    """
    Return certain column of a matrix.
    """
    return [row[column - 1] for row in matrix]
