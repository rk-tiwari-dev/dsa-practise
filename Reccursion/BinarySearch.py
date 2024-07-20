# binary search using recursion


def binarySearch(arr, low, high, key):
    if low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return binarySearch(arr, low, mid - 1, key)
        else:
            return binarySearch(arr, mid + 1, high, key)
    return -1


print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8, 5))  # 4
print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8, 10))  # -1
print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8, 1))  # 0
print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8, 9))  # 8
print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8, 3))  # 2
print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8, 6))  # 5
