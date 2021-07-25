import numpy as np

class Matrix:
    def __init__(self, matrix_string: str) -> None:

        self.matrix = np.array([
            [int(character) for character in row.split()]
            for row in matrix_string.splitlines()
        ])

    def row(self, row: int) -> list[int]:
        """
        Return a certain row of the matrix.
        """
        return self.matrix[row - 1,:]

    def column(self, column: int) -> list[int]:
        """
        Return a certain column of the matrix.
        """
        return self.matrix[:, column - 1]

m = Matrix("1 2 3 4\n5 6 7 8\n9 8 7 6")
print(m.row(3)[0]) # Output: 9
m.row(3)[0] = 5    
print(m.row(3)[0]) # Output: 5

print(m.column(3)[0]) # Output: 3
m.column(3)[0] = 5
print(m.column(3)[0]) # Output: 5
