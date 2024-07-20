from typing import List

# sorting the array and then using two pointer technique
# Time complexity: O(n^2)
# Space complexity: O(n)


def three_sum(nums: List[int], target: int) -> List[List[int]]:
    nums.sort()  # Sort the array to use two-pointer technique
    triplets = []

    for i in range(len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue  # Skip duplicate elements

        left, right = i + 1, len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == target:
                triplets.append([nums[i], nums[left], nums[right]])

                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1

    return triplets


# Example usage
nums = [-1, 0, 1, 2, -1, -4]
target = 0
result = three_sum(nums, target)
print(result)
