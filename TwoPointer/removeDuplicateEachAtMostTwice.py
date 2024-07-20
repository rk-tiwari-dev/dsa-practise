"""Given a sorted array, remove the duplicates in-place, such that each element in the array appears at most twice, and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Input format
There are two lines of input.

First line contains an integer n - Number of elements.

Second line contains n space separated integers - The array nums."""


def removeDuplicatesFromSortedArrayII(n, nums):
    i = 0
    for num in nums:
        if i < 2 or num > nums[i - 2]:
            nums[i] = num
            print("curr num is ", nums[i])
            i += 1
    return i, nums[:i]


arr1 = [1, 1, 1, 2, 2, 3]
n = 6
print(removeDuplicatesFromSortedArrayII(n, arr1))

# Time complexity: O(n)
# Space complexity: O(1)
