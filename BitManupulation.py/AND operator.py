# here need on AND bitwise oprator
# we can use the AND operator to find the 1's compliment of a number
# we can use the AND operator with a number that has all bits set to 1
# and then subtract the number from the result
# the number that has all bits set to 1 is 2 ** len(binary) - 1
# for example, if the number is 5, the binary number is 101
# the number that has all bits set to 1 is 111
# 111 - 101 = 010

x = 234
print(bin(x))
print(bin(x ^ ((1 << x.bit_length()) - 1)))
# it works as 1's compliment
print(bin(x & ((1 << x.bit_length()) - 1)))
# it works as 0's compliment

# OR oprator for bit manupulations

a = 6 | 7
print(a)

# AND oprator

b = 6 & 7
print(b)

# XOR oprator
c = 6 ^ 7
print(c)

# shift oprator
d = 6 << 7
print(d)

# NOT oprator

e = ~6
print(e)
