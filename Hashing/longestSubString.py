# python code for longest substring without repeating characters


def longestSubString(s):
    n = len(s)
    if n == 0:
        return 0
    if n == 1:
        return 1
    start = 0
    end = 0
    max_length = 0
    hash_map = {}
    while end < n:
        if s[end] in hash_map:
            start = max(start, hash_map[s[end]] + 1)
        hash_map[s[end]] = end
        max_length = max(max_length, end - start + 1)
        end += 1
    return max_length


print(longestSubString("abcabcbb"))  # 3
print(longestSubString("bbbb"))  # 1
print(longestSubString("pwwkew"))  # 3
print(longestSubString(""))  # 0
print(longestSubString(" "))  # 1
print(longestSubString("au"))  # 2
print(longestSubString("dvdf"))  # 3
print(longestSubString("abba"))  # 2
print(longestSubString("tmmzuxt"))  # 5
