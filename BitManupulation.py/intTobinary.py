def intTobinary(integer):
    binary = ""
    while integer > 0:
        binary = str(integer % 2) + binary
        integer = integer // 2
    return binary


print(intTobinary(10))  # 1010
print(intTobinary(20))  # 10100
print(intTobinary(30))  # 11110
