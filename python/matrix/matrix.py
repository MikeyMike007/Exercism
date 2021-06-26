class Matrix:
    def __init__(self, matrix_string):
        self.matrix = convert_matrix(matrix_string)

    def row(self, index):
        return self.matrix[index-1][:]

    def column(self, index):
        return self.matrix[:][index - 1]

def convert_matrix(matrix_string):
    matrix = []
    row = []
    length = len(matrix_string)

    for element in matrix_string:
        print(f"Element is {element}\n")
        print(f"Length is {length}\n")
        if element == '\n':
            matrix.append(row)
            row = []
        elif element == ' ':
            continue
        else:
            row.append(int(element))

    matrix.append(row)
    return matrix

matrix = Matrix("1 2 3\n 1 2 3\n 3 2 1 \n 2 3 4\n 1 2 3")
print(matrix.matrix)
print(matrix.row(2))
print(matrix.column(3))
