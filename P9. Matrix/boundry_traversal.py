# This program performs boundary traversal of a 2D matrix.
# It prints all the elements on the boundary of the matrix
# in a clockwise order starting from the top-left corner.

def boundary_traversal(mat):
    # Define the number of rows and columns
    R = len(mat)
    C = len(mat[0])
    
    # If the matrix has only one row
    if R == 1:
        for i in range(C):
            print(mat[0][i], end=" ")
    # If the matrix has only one column
    elif C == 1:
        for i in range(R):
            print(mat[i][0], end=" ")
    else:
        # Traverse the top row
        for i in range(C):
            print(mat[0][i], end=" ")
        
        # Traverse the right column
        for i in range(1, R):
            print(mat[i][C-1], end=" ")
        
        # Traverse the bottom row in reverse
        for i in range(C-2, -1, -1):
            print(mat[R-1][i], end=" ")
        
        # Traverse the left column in reverse
        for i in range(R-2, 0, -1):
            print(mat[i][0], end=" ")

# Example usage
if __name__ == "__main__":
    arr = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]

    # Call the boundary traversal function
    boundary_traversal(arr)

'''
#Input
1  2  3  4
5  6  7  8
9 10 11 12
13 14 15 16

# Output
1 2 3 4 8 12 16 15 14 13 9 5
'''