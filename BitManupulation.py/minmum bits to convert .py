def minBitstoConvert(a, b):
    print(bin(a))
    print(bin(b))
    count = 0
    c = a ^ b
    while c:
        print('here the c ',bin(c))
        count += c & 1
        print('count',count)
        c >>= 1
    return count


"""expalanations :
1. First we will take xor of a and b and store it in c.
2. Then we will count the number of set bits in c and return the count.
3. We will do this by using a while loop and incrementing the count by 1 if the last bit of c is 1.
 4. Then we will right shift c by 1 bit.
 5. We will continue this process until c becomes 0.
 6. Finally we will return the count."""


print(minBitstoConvert(5, 10))
print(minBitstoConvert(10, 20))
print(minBitstoConvert(4,0))
