# sum of all digits using recusrion
def sumOfDigits(n):
    if n == 0:
        return 0
    return n % 10 + sumOfDigits(n // 10)


print(sumOfDigits(12345))  # 15
print(sumOfDigits(123456789))  # 45
