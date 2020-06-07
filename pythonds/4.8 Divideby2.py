"""
Stack:
convert integer values into binary numbers

"""

from Stack import Stack

def divideby2(decnumber):
    bin = Stack()
    while decnumber > 0:
        decnumber, rem = divmod(decnumber, 2)
        # rem = decnumber % 2
        # decnumber = decnumber // 2
        bin.push(rem)

    binstring = ""
    while not bin.isEmpty():
        binstring = binstring + str(bin.pop())

    return binstring

print(divideby2(42))

# general case

def baseConver(decnumber, base):

    digits = "0123456789ABCDEF"

    bin = Stack()
    while decnumber > 0:
        decnumber, rem = divmod(decnumber, base)
        # rem = decnumber % 2
        # decnumber = decnumber // 2
        bin.push(rem)

    binstring = ""
    while not bin.isEmpty():
        binstring = binstring + digits[bin.pop()]

    return binstring


print(baseConver(42, 16))
print(baseConver(233, 16))
print(baseConver(25, 8))
print(baseConver(26, 26))





