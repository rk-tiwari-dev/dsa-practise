def firstUniqueInteger(lis: List[int]) -> int:
    count_map = {}
    for num in lis:
        count_map[num] += 1

    for num in lis:
        if count_map[num] == 1:
            return num

    return -1
