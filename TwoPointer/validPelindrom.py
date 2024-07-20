# problem validPelindrom.py
# # problem: Valid Palindrome
# # Given a string, the task is to check whether the given string is a palindrome or not.


def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True


print(isPalindrome("assa"))  # True
print(isPalindrome("qwerttrewq"))  # True
print(isPalindrome("qwerttrew"))  # False
