def twoNonrepeatingNumber(arr):
    xor = 0
    for i in arr:
        xor ^= i
    rightmostSetBit = xor & ~(xor - 1)
    x = 0
    y = 0
    for i in arr:
        if i & rightmostSetBit:
            x ^= i
        else:
            y ^= i
    return x, y


# expalnation
# 1. xor of all element will give xor of two non repeating element
# 2. find rightmost set bit in xor
# 3. divide array in two group based on rightmost set bit
# 4. xor of each group will give two non repeating element
