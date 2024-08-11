def convertOneToAnother(a, b):
    count = 0
    c = a ^ b
    while c:
        count += 1
        c &= c - 1
    return count
