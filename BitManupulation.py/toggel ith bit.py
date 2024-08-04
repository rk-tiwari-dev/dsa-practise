def toggeleIthbit(n, i):
    print("given int = ", bin(n))
    return bin(n ^ (1 << i))


print(toggeleIthbit(5, 1))
print(toggeleIthbit(5, 2))
