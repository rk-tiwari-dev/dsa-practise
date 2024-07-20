# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of the line i are at (i, ai) and (i, 0).
# Find two lines that together with the x-axis form a container that holds the most water.
# Return the maximum area of water it can contain.
# Example:
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
# In this case, the max area of water (blue section) the container can contain is 49.
# Approach:
# Initialize two pointers left and right to the first and last element of the array respectively.
# Initialize a variable max_area to store the maximum area of water.
# Traverse the array until the left pointer is less than the right pointer.
# Calculate the area of water between the left and right pointers using the formula:
# area = min(arr[left], arr[right]) * (right - left)
# Update the max_area if the area is greater than the max_area.
# If the element at the left pointer is less than the element at the right pointer, then move the left pointer to the next element.
# Otherwise, move the right pointer to the previous element.
# Repeat the above steps until the left pointer is less than the right pointer.
# Return the max_area.
# Below is the implementation of the above approach:


def maxArea(arr):
    left = 0
    right = len(arr) - 1
    max_area = 0
    while left < right:
        area = min(arr[left], arr[right]) * (right - left)
        max_area = max(max_area, area)
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return max_area


print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49
# Output:
# 49
# Time Complexity: O(N)
# Auxiliary Space: O(1)
