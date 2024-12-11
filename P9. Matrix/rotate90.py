def rotate90(mat):
    n = len(mat)
    # Create a temporary matrix to store the rotated version
    temp = [[0] * n for _ in range(n)]
    
    # Rotate the matrix by 90 degrees using a temporary matrix
    for i in range(n):
        for j in range(n):
            temp[n - j - 1][i] = mat[i][j]
    
    # Copy the rotated matrix back to the original matrix
    for i in range(n):
        for j in range(n):
            mat[i][j] = temp[i][j]


def swap(mat, i, j):
    temp = mat[i][j]
    mat[i][j] = mat[j][i]
    mat[j][i] = temp


def swap2(low, high, i, mat):
    temp = mat[low][i]
    mat[low][i] = mat[high][i]
    mat[high][i] = temp


def rotate90Deg(mat):
    n = len(mat)
    
    # Step 1: Transpose the matrix (swap mat[i][j] with mat[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            swap(mat, i, j)
    
    # Step 2: Reverse each column
    for i in range(n):
        low, high = 0, n - 1
        while low < high:
            swap2(low, high, i, mat)
            low += 1
            high -= 1


# Example usage
arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

rotate90Deg(arr)

# Print the rotated matrix
for row in arr:
    print(' '.join(map(str, row)))
