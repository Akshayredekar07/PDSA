

def max_item(arr):
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val

def max_range(arr, start, end):
    if end < start:
        return -1
    if arr is None or len(arr) == 0:
        return -1

    max_val = arr[start]
    for i in range(start, end + 1):
        if arr[i] > max_val:
            max_val = arr[i]
    return max_val

if __name__ == "__main__":
    arr = [1, 3, 2, 9, 18]
    print(max_item(arr))  # Max value in the array
    print(max_range(arr, 1, 3))  # Max value in the range (index 1 to 3)
