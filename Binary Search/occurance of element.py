def countOccurrences(n, arr, k):
    def findBoundary(arr, n, k, searchFirst):
        left, right = 0, n - 1
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == k:
                result = mid
                if (
                    searchFirst
                ):  # search towards left and it has logic to move right pointer and find the first occurance
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < k:
                left = mid + 1
            else:
                right = mid - 1
        return result

    firstIndex = findBoundary(arr, n, k, True)
    if firstIndex == -1:
        return 0
    lastIndex = findBoundary(arr, n, k, False)
    return lastIndex - firstIndex + 1
