def twoSum(arr, target):
    num_to_index = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_to_index:
            return sorted([num_to_index[complement], i])
        num_to_index[num] = i
    return []


print(twoSum([2, 7, 11, 15], 9))  # [0, 1]
print(twoSum([3, 2, 4], 6))  # [1, 2]
print(twoSum([3, 3], 6))  # [0, 1]
# Time complexity: O(n)
# Space complexity: O(n)
# n is the length of the array
# This algorithm is similar to the
# TwoPointer/TwoSumSorted.py
