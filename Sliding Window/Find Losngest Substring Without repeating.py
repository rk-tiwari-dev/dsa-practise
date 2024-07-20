"""Problem Description
Given a string, find the length of the longest substring which has no repeating characters.

Input format
Input is a string.

Output format
Output is an integer representing the longest substring with no repeating characters.

Sample Input 1
aabcccbcb

Sample Output 1
3

Explanation 1
"abc" is the longest substring with no repeating characters.

Sample Input 2
cdddddd

Sample Output 2
2

Explanation 2
"cd" is the longest substring with no repeating characters."""

from typing import Set


def length_of_longest_substring(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0

    char_set: Set[str] = set()
    left = 0
    max_length = 0

    for right in range(n):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# Read input
s = input().strip()

# Get the result
result = length_of_longest_substring(s)

# Print the result
print(result)
