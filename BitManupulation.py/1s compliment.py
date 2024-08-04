# without using bitwise operator
def oneComplimnet(num):
    binary = bin(num)[2:]
    oneCompliment = ""
    for i in binary:
        if i == "1":
            oneCompliment += "0"
        else:
            oneCompliment += "1"
    return int(oneCompliment, 2)


# we need to convert the number to binary and then find the 1's compliment of the binary number
# and then convert the 1's compliment back to integer
# we also want the one's compliment to be in the same length as the original binary number

print(oneComplimnet(5))  # 2
print(oneComplimnet(10))  # 5
print(oneComplimnet(20))  # 11


def oneComplimnetBinaryform(num):
    binary = bin(num)[2:]
    oneCompliment = ""
    for i in binary:
        if i == "1":
            oneCompliment += "0"
        else:
            oneCompliment += "1"
    return oneCompliment


print(oneComplimnetBinaryform(5))  # 10
print(oneComplimnetBinaryform(10))  # 101
print(oneComplimnetBinaryform(20))  # 10100
# the above function returns the binary form of the 1's compliment of the number
