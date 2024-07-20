from typing import Dict, List


def largestSubarraySumZero(n: int, arr: List[int]) -> List[int]:
    hash_map: Dict[int, int] = {}
    max_len = 0
    curr_sum = 0
    start_index = -1
    end_index = -1

    for i in range(n):
        curr_sum += arr[i]

        if curr_sum == 0:
            max_len = i + 1
            start_index = 0
            end_index = i

        if curr_sum in hash_map:
            if i - hash_map[curr_sum] > max_len:
                max_len = i - hash_map[curr_sum]
                start_index = hash_map[curr_sum] + 1
                end_index = i
        else:
            hash_map[curr_sum] = i

    if max_len == 0:
        return [-1]

    return arr[start_index : end_index + 1]


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    result = largestSubarraySumZero(n, arr)
    print(*result)


if __name__ == "__main__":
    main()
