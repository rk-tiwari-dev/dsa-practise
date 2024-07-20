# factorial of a number using reccursion


def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # 120
print(factorial(10))  # 3628800
print(factorial(0))  # 1
print(factorial(1))  # 1
print(factorial(2))  # 2
print(factorial(3))  # 6
print(factorial(4))  # 24
print(factorial(6))  # 720
