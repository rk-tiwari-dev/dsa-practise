from collections import Counter
from typing import List


def find_anagrams(p: str, s: str) -> List[int]:
    len_p, len_s = len(p), len(s)

    if len_p > len_s:
        return []

    # Frequency count of characters in pattern p
    p_count = Counter(p)

    # Initial frequency count of the first window in s
    window_count = Counter(s[:len_p])

    result_indices = []

    # Check the first window
    if window_count == p_count:
        result_indices.append(0)

    # Slide the window across the string s
    for i in range(len_p, len_s):
        # Add the new character to the window
        window_count[s[i]] += 1

        # Remove the old character from the window
        old_char = s[i - len_p]
        if window_count[old_char] == 1:
            del window_count[old_char]
        else:
            window_count[old_char] -= 1

        # Compare window_count with p_count
        if window_count == p_count:
            result_indices.append(i - len_p + 1)

    return result_indices


def main():
    s, p = input().split()
    answer = find_anagrams(p, s)
    print(len(answer))
    print(" ".join([str(i) for i in answer]))


if __name__ == "__main__":
    main()
