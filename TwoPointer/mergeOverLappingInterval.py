"""Problem Description
An interval is a range, with a starting value and ending value. [1, 3] indicates elements 1, 2, 3 and so on.
Given a collection of intervals, merge all overlapping intervals. 
The result should only have mutually exclusive intervals -
meaning that no number should be common between two intervals, in the result.
Note: The merged intervals should be printed in increasing order of start value.
Input format
There are N+1 lines of input.
First line contains N, the number of intervals
Next N lines contain 2 space separated integers A and B, which represent the start and end of an interval
Output format
For the X merged intervals, print each interval (the start and end being space separated) on a separate line
Constraints
1 <= N <= 50000
0 <= A, B <= 1e9
B >= A
Sample Input 1
4
1 3
2 6
8 10
15 18
Sample Output 1
1 6
8 10
15 18"""

from typing import List


def mergeIntervals(nums: List[List[int]]) -> List[List[int]]:
    nums.sort(key=lambda x: x[0])
    merged_intervals: List[List[int]] = []
    for interval in nums:
        if not merged_intervals or merged_intervals[-1][1] < interval[0]:
            merged_intervals.append(interval)
        else:
            # There is an overlap, so merge the current interval with the last merged interval
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

    # Step 4: Return the list of merged intervals
    return merged_intervals


print(mergeIntervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
# Time complexity: O(nlogn)
# Space complexity: O(1)
