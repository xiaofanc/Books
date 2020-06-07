"""
Recursion: stack frame

Suppose that instead of concatenating the result of the recursive call to toStr with the string from convertString, we modified our algorithm to push the strings onto a stack instead of making the recursive call. 

"""

from Stack import Stack

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    rstack = Stack()

    while n > 0:
        if n < base:
            rstack.push(convertString[n])
        else:
            rstack.push(convertString[n % base])
        n = n // base

    res = ""
    while not rstack.isEmpty():
        res = res + str(rstack.pop())

    return res

print(toStr(2, 2))        # 10
print(toStr(42, 16))      # 2A
print(toStr(233, 16))     # E9
print(toStr(25, 8))       # 31
print(toStr(26, 26))      # 10


