# two sum sorted array
# Given a sorted array and a target sum, the task is to find the pair of elements whose sum is equal to the target sum.
# Example:
# Input: arr[] = {2, 3, 4, 5, 6, 7, 8}, target = 10
# Output: (2, 8)
# Input: arr[] = {2, 3, 4, 5, 6, 7, 8}, target = 14
# Output: (6, 8)
# Approach:
# Initialize two pointers left and right to the first and last element of the array respectively.
# Traverse the array until the left pointer is less than the right pointer.
# If the sum of the elements at the left and right pointers is equal to the target sum, then return the pair of elements.
# If the sum of the elements at the left and right pointers is less than the target sum, then move the left pointer to the next element.
# Otherwise, move the right pointer to the previous element.
# Repeat the above steps until the left pointer is less than the right pointer.
# If no such pair is found, then return -1.
# Below is the implementation of the above approach:


def twoSum(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] + arr[right] == target:
            return (arr[left], arr[right])
        elif arr[left] + arr[right] < target:
            left += 1
        else:
            right -= 1
    return -1


print(twoSum([2, 3, 4, 5, 6, 7, 8], 10))  # (2, 8)
print(twoSum([2, 3, 4, 5, 6, 7, 8], 14))  # (6, 8)
# Output:
# (2, 8)
# (6, 8)
# Time Complexity: O(N)
# Auxiliary Space: O(1)
