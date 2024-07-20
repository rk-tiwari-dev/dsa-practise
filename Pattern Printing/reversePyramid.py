def reversePyramid(n):
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))
        # increase space by 1 in each iteration


print(reversePyramid(5))
