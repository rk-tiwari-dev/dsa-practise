from typing import List


def findPeakElement(nums: List[int]) -> int:
    if len(nums) == 1:
        return 0
    if len(nums) == 2:
        return 0 if nums[0] > nums[1] else 1
    l, r = 0, len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid] > nums[mid + 1]:
            r = mid
        else:
            l = mid + 1
    return l


print(findPeakElement([1, 2, 3, 1]))  # 2
print(findPeakElement([1, 2, 1, 3, 5, 6, 4]))  # 5
print(findPeakElement([1]))  # 0
