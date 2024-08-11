def largestNumber(nums):
    nums = list(map(str, nums))
    nums.sort(key=lambda x: x * 10, reverse=True)
    result = "".join(nums)
    return result


print(largestNumber([3, 30, 34, 5, 9]))  # 9534330
print(largestNumber([10, 2]))  # 210
print(largestNumber([0, 0]))  # 0