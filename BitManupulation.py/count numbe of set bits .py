def countNumofSetbits(n):
    count = 0
    print(bin(n))
    while n:
        n = n & (n-1)
        count += 1
    return count


print(countNumofSetbits(10))
print(countNumofSetbits(20))