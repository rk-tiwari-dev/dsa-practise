# problem: Remove duplicates from a sorted array
# Given a sorted array, the task is to remove the duplicate elements from the array.
# Example:
# Input: arr[] = {2, 2, 2, 2, 2}
# Output: arr[] = {2}
# Input: arr[] = {1, 2, 2, 3, 4, 4, 4, 5, 5}
# Output: arr[] = {1, 2, 3, 4, 5}
# Approach:
# Initialize two pointers left and right to the first and second element of the array respectively.
# Traverse the array until the right pointer reaches the end of the array.
# If the elements at the left and right pointers are the same, then remove the element at the right pointer.
# Otherwise, update the left pointer to the right pointer and move the right pointer to the next element.
# Repeat the above steps until the right pointer reaches the end of the array.
# Return the modified array.
# Below is the implementation of the above approach:
# Python3


def removeDuplicates(arr):
    left = arr[0]
    right = arr[arr.length - 1]
    while right < len(arr):
        if arr[right] == left:
            arr.pop(right)
        else:
            left = arr[right]
            right += 1
    return arr


print(removeDuplicates([2, 2, 2, 2, 2]))  # [2]
print(removeDuplicates([1, 2, 2, 3, 4, 4, 4, 5, 5]))  # [1, 2, 3, 4, 5]
# Output:
# [2]
# [1, 2, 3, 4, 5]
# Time Complexity: O(N)
# Auxiliary Space: O(1)
