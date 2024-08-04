def binaryToint(binary):
    integer = 0
    for i in range(len(binary)):
        integer += int(binary[i]) * 2 ** (
            len(binary) - i - 1
        )  # 2 ** (len(binary) - i - 1) is the power of 2
        # starts from the rightmost bit and goes to the leftmost bit
    return integer


print(binaryToint("1010"))  # 10
print(binaryToint("10100"))  # 20
print(binaryToint("11110"))  # 30
