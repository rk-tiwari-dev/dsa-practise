# problem states: Reverse a string
# Given a string, the task is to reverse the string.
# Example:
# Input: str = "geeksforgeeks"
# Output: "skeegrofskeeg"
# Input: str = "hello"
# Output: "olleh"
# Approach:
# Initialize two pointers left and right to the first and last element of the string respectively.
# Traverse the string until the left pointer is less than the right pointer.
# Swap the elements at the left and right pointers.
# Move the left pointer to the next element and the right pointer to the previous element.
# Repeat the above steps until the left pointer is less than the right pointer.
# Return the modified string.
# Below is the implementation of the above approach:


def reverseString(s):
    s = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return "".join(s)


print(reverseString("geeksforgeeks"))  # skeegrofskeeg
print(reverseString("hello"))  # olleh
