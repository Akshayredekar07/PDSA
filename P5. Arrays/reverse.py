
def reverse_array(arr):
    s = 0
    e = len(arr) - 1
    while s < e:
        arr[s], arr[e] = arr[e], arr[s]  
        s += 1
        e -= 1
    return arr

if __name__ == "__main__":
    arr = [10, 5, 7, 30]
    reversed_arr = reverse_array(arr)
    print(" ".join(map(str, reversed_arr)))

# def reverse_array(arr):
#     return arr[::-1] 

# if __name__ == "__main__":
#     arr = [10, 5, 7, 30]
#     reversed_arr = reverse_array(arr)
#     print(" ".join(map(str, reversed_arr)))
