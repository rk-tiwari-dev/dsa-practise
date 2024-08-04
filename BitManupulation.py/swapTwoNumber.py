def swapTwoNumber(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


"""this works as follows: 
  xor of a and b is stored in a
  and then xor of a and b is stored in b
  and then xor of a and b is stored in a
  and then return a and b"""
print(swapTwoNumber(5, 6))
print(swapTwoNumber(10, 20))
print(swapTwoNumber(100, 200))
