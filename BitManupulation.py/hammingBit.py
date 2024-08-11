def hammingBin(n):
    count = 0
    while n:
        count += 1
        n &= n - 1
    return count


print(hammingBin(9))  # 2
print(hammingBin(10))  # 2
