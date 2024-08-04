def removeRightsetBit(n):
    print(bin(n))
    return bin(n & (n - 1))


print(removeRightsetBit(10))
print(removeRightsetBit(20))
print(removeRightsetBit(100))
