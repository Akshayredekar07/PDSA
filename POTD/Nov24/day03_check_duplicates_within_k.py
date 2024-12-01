def check_duplicates_within_k(arr, k):
    seen = set()

    for i in range(len(arr)):
        # Check if the current element is already in the set
        if arr[i] in seen:
            return True
        # Add the current element to the set
        seen.add(arr[i])

        # Maintain the set size to be at most k
        if i >= k:
            seen.remove(arr[i - k])

    return False

# Example usage
arr = [1, 2, 3, 1]
k = 3
result = check_duplicates_within_k(arr, k)
print("Contains duplicates within k:", result)
