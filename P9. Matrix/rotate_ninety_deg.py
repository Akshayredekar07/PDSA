# Function to rotate the matrix by 90 degrees (simple approach)
def rotate_90(mat):
    n = len(mat)
    # Create a temporary matrix
    temp = [[0] * n for _ in range(n)]

    # Copy the rotated elements to the temp matrix
    for i in range(n):
        for j in range(n):
            temp[n - j - 1][i] = mat[i][j]

    # Copy back the rotated matrix to the original matrix
    for i in range(n):
        for j in range(n):
            mat[i][j] = temp[i][j]

# Function to rotate the matrix by 90 degrees efficiently (in-place)
def rotate_90_in_place(mat):
    n = len(mat)

    # Transpose the matrix
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

    # Reverse each column
    for i in range(n):
        low, high = 0, n - 1
        while low < high:
            mat[low][i], mat[high][i] = mat[high][i], mat[low][i]
            low += 1
            high -= 1

# Function to print the matrix
def print_matrix(mat):
    for row in mat:
        print(" ".join(map(str, row)))
    print()

# Example usage
if __name__ == "__main__":
    arr = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    print("Original Matrix:")
    print_matrix(arr)

    # Rotate using the efficient in-place method
    rotate_90_in_place(arr)

    print("Matrix After 90 Degree Rotation:")
    print_matrix(arr)

'''
Original Matrix:
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

Matrix After 90 Degree Rotation:
13 9 5 1
14 10 6 2
15 11 7 3
16 12 8 4

'''