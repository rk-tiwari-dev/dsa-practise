arr1 = [
    1,
    2,
    3,
    4,
    53,
    2,
    4,
    23,
    78,
]
# https://www.geeksforgeeks.org/find-maximum-sum-triplets-array-j-k-ai-aj-ak/


def maxSumTriplet(n, arr) -> int:
    ans = 0
    for i in range(1, (n - 1)):
        max1 = 0
        max2 = 0
        for j in range(0, i):
            if arr[j] < arr[i]:
                max1 = max(max1, arr[j])
        for j in range((i + 1), n):
            if arr[j] > arr[i]:
                max2 = max(max2, arr[j])
                if max1 > 0 and max2 > 0:
                    ans = max(ans, max1 + arr[i] + max2)

    return ans


print(maxSumTriplet(len(arr1), arr1))

# worst case time complexity is O(n^2) and space complexity is O(1)
# above approach is not optimal
