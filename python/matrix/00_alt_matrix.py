class Matrix:
    def __init__(self, matrix_string: str) -> None:

        self.matrix = [
            [int(character) for character in row.split()]
            for row in matrix_string.splitlines()
        ]

    def row(self, row: int) -> list[int]:
        """
        Return a certain row of the matrix.
        """
        return self.matrix[row - 1]

    def column(self, column: int) -> list[int]:
        """
        Return a certain column of the matrix.
        """
        return [row[column - 1] for row in self.matrix]

