def matrix_multiplication(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        return "Matrix multiplication not possible"
    else:
        result = [[0 for i in range(len(mat2[0]))] for j in range(len(mat1))]
        for i in range(len(mat1)):
            for j in range(len(mat2[0])):
                for k in range(len(mat2)):
                    result[i][j] += mat1[i][k] * mat2[k][j]
        return result

    mat1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    mat2 = [[1, 2], [3, 4], [5, 6]]

    print(matrix_multiplication(mat1, mat2))
    # Output: [[22, 28], [49, 64], [76, 100]]
    # Time complexity: O(n^3)
    # Space complexity: O(n^2)
    # where n is the number of rows in mat1 and number of columns in mat2
