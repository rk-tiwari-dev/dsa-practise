# resursive functions for sum of n numbers
def sumOfN(n):
    if n == 0:
        return 0
    return n + sumOfN(n - 1)


print(sumOfN(5))  # 15
print(sumOfN(10))  # 55
