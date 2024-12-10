
def insert(arr, n, key, pos, cap):
    """
    Inserts an element into the array at a specified position.

    Parameters:
    arr (list): The array to insert into.
    n (int): The current size of the array.
    key (int): The element to insert.
    pos (int): The position at which to insert the element (1-based index).
    cap (int): The maximum capacity of the array.

    Returns:
    int: The new size of the array after insertion.
    """
    # O(n) time
    if n == cap:
        return n
    if pos < 1 or pos > n + 1:
        print("Invalid position for insertion.")
        return n
    
    index = pos - 1  # Convert to 0-based index
    # Shift elements to the right to make space for the new element
    for i in range(n - 1, index - 1, -1):
        arr[i + 1] = arr[i]
    
    arr[index] = key  # Insert the element at the specified position
    return n + 1  # Return the new size of the array

def main():

    arr = [20, 7, 5, 25, 34, 21, 41]
    
    array = [0] * 10  # Example array with a capacity of 10
    size = 5  # Initial size of the array
    capacity = 10  # Maximum capacity of the array

    # Initial array elements
    array[0] = 10
    array[1] = 20
    array[2] = 30
    array[3] = 40
    array[4] = 50

    print("Original Array:")
    for i in range(size):
        print(array[i], end=" ")

    key = 25  # Element to be inserted
    position = 3  # Position where the element should be inserted

    size = insert(array, size, key, position, capacity)

    print("\nArray after insertion:")
    for i in range(size):
        print(array[i], end=" ")

if __name__ == "__main__":
    main()

