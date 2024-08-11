# find fisrt and last occurance using binary search
# Time complexity: O(logn)
# Space complexity: O(1)


def firstlastoccuranceBinarySearch(arr, n, x):
    first = -1
    last = -1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            first = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            last = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return first, last


arr = [1, 3, 5, 5, 5, 5, 67, 123, 125]
n = len(arr)
x = 5
print(firstlastoccuranceBinarySearch(arr, n, x))
