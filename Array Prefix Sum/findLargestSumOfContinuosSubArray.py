def largestSumOfSubArray(arr):
    maxSum = arr[0]
    currentSum = arr[0]
    for i in range(1, len(arr)):
        currentSum = max(arr[i], currentSum + arr[i])
        maxSum = max(maxSum, currentSum)
    return maxSum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(largestSumOfSubArray(arr))
# Time complexity: O(n)
# Space complexity: O(1)
# n is the length of the array
# This algorithm is similar to the
# ArrayPrefixSum/FindLargestSumOfContinuosSubArray.py
