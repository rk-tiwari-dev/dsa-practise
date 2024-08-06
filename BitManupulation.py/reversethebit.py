# Reverse the bits of a given 32 bits unsigned integer.(always posetive number)


def reverseBits(N: int) -> int:
    result = 0
    for i in range(32):
        # Extract the rightmost bit of N and add it to the result
        result = (result << 1) | (N & 1)
        # Shift N right to process the next bit in the next iteration
        N >>= 1
    return result


print(reverseBits(43261596))
print(reverseBits(4294967293))
print(reverseBits(0))
