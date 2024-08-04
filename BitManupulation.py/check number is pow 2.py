def checkNumisPowof2(n):
    print(bin(n))
    if n == 0:
        return False
    return (n & (n - 1)) == 0


print(checkNumisPowof2(16))
print(checkNumisPowof2(15))
print(checkNumisPowof2(0))
