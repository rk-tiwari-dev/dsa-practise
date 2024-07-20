# print the * pattern
def pattern(n):
    if n == 0:
        return
    pattern(n - 1)
    print("*" * n)


print(pattern(5))
# Output:
# *
# **
# ***
# ****
# *****
