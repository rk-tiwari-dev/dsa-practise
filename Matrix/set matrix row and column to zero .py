def setMatrixRowCoulmnToZero(matrix):
    row = [False] * len(matrix)
    column = [False] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                column[j] = True
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if row[i] or column[j]:
                matrix[i][j] = 0
    return matrix


mat1 = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
mat2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


print(setMatrixRowCoulmnToZero(mat1))
# Output: [[1, 0, 3], [0, 0, 0], [7, 0, 9]]
print(setMatrixRowCoulmnToZero(mat2))
# Output: [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
# Time complexity: O(m*n)