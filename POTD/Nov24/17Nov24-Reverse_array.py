# Python implementations of all the approaches for reversing an array:

# 1. Brute Force Approach
# This creates a new array and explicitly copies elements from the original array in reverse order.

def reverse_array_brute_force(arr):
    n = len(arr)
    rev = [0] * n  # Create a new array of the same size

    for i in range(n):
        rev[i] = arr[n - 1 - i]  # Copy elements in reverse order

    return rev

# Example usage
arr = [1, 2, 3, 4, 5]
print(reverse_array_brute_force(arr))  # Output: [5, 4, 3, 2, 1]

# Time Complexity: O(n)  
# Space Complexity: O(n)

# 2. Two-Loop Swapping Approach
# This uses nested loops to reverse the array in place.

def reverse_array_two_loops(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            if j == n - i - 1:  # Find the corresponding element
                arr[i], arr[j] = arr[j], arr[i]  # Swap elements

# Example usage
arr = [1, 2, 3, 4, 5]
reverse_array_two_loops(arr)
print(arr)  # Output: [5, 4, 3, 2, 1]

# Time Complexity: O(n^2)  
# Space Complexity: O(1)

# 3. In-Place Iterative Approach
# This approach uses two pointers to reverse the array in place.

def reverse_array_in_place(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]  # Swap elements
        left += 1
        right -= 1

# Example usage
arr = [1, 2, 3, 4, 5]
reverse_array_in_place(arr)
print(arr)  # Output: [5, 4, 3, 2, 1]

# Time Complexity: O(n)  
# Space Complexity: O(1)

# 4. Using Python Slicing
# This is a concise way to reverse an array in Python. It creates a new reversed list.

def reverse_array_slicing(arr):
    return arr[::-1]

# Example usage
arr = [1, 2, 3, 4, 5]
print(reverse_array_slicing(arr))  # Output: [5, 4, 3, 2, 1]

# Time Complexity: O(n)  
# Space Complexity: O(n)

# Comparison of Approaches
# | Approach             | Time Complexity | Space Complexity | Description               |
# |----------------------|------------------|------------------|---------------------------|
# | Brute Force          | O(n)             | O(n)             | Creates a new array.     |
# | Two-Loop Swapping    | O(n^2)           | O(1)             | Uses redundant iterations.|
# | In-Place Iterative   | O(n)             | O(1)             | Efficient and modifies in-place. |
# | Slicing              | O(n)             | O(n)             | Quick and Pythonic.      |

