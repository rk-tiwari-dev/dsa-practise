# given array is rotete sorted array on a pivot point
def findInRotatedArray(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


print(findInRotatedArray([4, 5, 6, 7, 0, 1, 2], 0))  # 4
print(findInRotatedArray([4, 5, 6, 7, 0, 1, 2], 3))  # -1
print(findInRotatedArray([1], 0))  # -1

"""The function `findInRotatedArray` is designed to locate the index of a `target` value in a rotated sorted array using binary search. Here’s a detailed breakdown of how it works:

### Function Definition:

```python
def findInRotatedArray(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1
```

### Explanation:

1. **Initialization:**
   - `left` and `right` are initialized to point to the start and end of the array, respectively.

2. **Binary Search Loop:**
   - The loop continues while `left` is less than or equal to `right`.

3. **Calculate the Midpoint:**
   - `mid` is calculated as the average of `left` and `right`.

4. **Check if Midpoint is the Target:**
   - If `nums[mid]` equals `target`, the function returns `mid` as the index where the target is found.

5. **Determine Which Side is Sorted:**
   - The array is split into two parts around `mid`. One of these parts will be sorted:
     - **If the left part is sorted:** 
       - This is true if `nums[left] <= nums[mid]`.
       - Check if the `target` lies within this sorted part (`nums[left] <= target <= nums[mid]`).
         - If it does, adjust `right` to `mid - 1` to search in the left half.
         - If it does not, adjust `left` to `mid + 1` to search in the right half.
     - **If the right part is sorted:**
       - This is true if `nums[mid] < nums[right]` (or if the left part is not sorted).
       - Check if the `target` lies within this sorted part (`nums[mid] <= target <= nums[right]`).
         - If it does, adjust `left` to `mid + 1` to search in the right half.
         - If it does not, adjust `right` to `mid - 1` to search in the left half.

6. **Target Not Found:**
   - If the loop exits without finding the `target`, the function returns `-1`.

### Example Walkthrough:

Consider an example array `[4, 5, 6, 7, 0, 1, 2]` with `target = 0`.

- **Initial Values:**
  - `left = 0`
  - `right = 6` (index of last element)

- **First Iteration:**
  - Calculate `mid = (0 + 6) // 2 = 3`
  - `nums[mid] = 7`
  - Since `nums[left] = 4` and `nums[mid] = 7`, the left part `[4, 5, 6, 7]` is sorted.
  - `target = 0` is not in the range `[4, 7]`, so search in the right half:
    - Update `left = mid + 1 = 4`

- **Second Iteration:**
  - Calculate `mid = (4 + 6) // 2 = 5`
  - `nums[mid] = 1`
  - Since `nums[left] = 0` and `nums[mid] = 1`, the left part `[0, 1]` is sorted.
  - `target = 0` is within the range `[0, 1]`, so search in the left half:
    - Update `right = mid - 1 = 4`

- **Third Iteration:**
  - Calculate `mid = (4 + 4) // 2 = 4`
  - `nums[mid] = 0`
  - `nums[mid]` equals `target`, so return `4`.

### Summary:

- **Sorted Array Segments:** The function leverages the fact that one of the segments (either left or right of `mid`) is always sorted, allowing efficient narrowing down of the search space.
- **Efficiency:** This approach maintains O(log n) time complexity due to the binary search mechanism, making it suitable for large arrays.

This method efficiently finds the target value in a rotated sorted array by combining binary search principles with an understanding of the rotation point."""
