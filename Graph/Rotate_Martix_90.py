def Rotate_Matrix_90(mat):
    n = len(mat)
    m = len(mat[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = mat[i][j]
    return result

'''
mat = [[0, 1], [1, 0], [1, 1]]
print(Rotate_Matrix_90(mat))

>> [[1, 1, 0], [1, 0, 1]]

[[0, 1],
 [1, 0],
 [1, 1]]

 [[1, 1, 0],
  [1, 0, 1]]

'''