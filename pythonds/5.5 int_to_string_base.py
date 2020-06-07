"""
recursion:
Converting an Integer to a String in Any Base
check 4.8 Divideby2.py

"""

def toStr(n, base):
    convertString = "0123456789ABCDEF"

    if n < base:
        return convertString[n]
    else:  # reverse
        return toStr(n // base, base) + convertString[n % base]

print(toStr(2, 2))        # 10
print(toStr(42, 16))      # 2A
print(toStr(233, 16))     # E9
print(toStr(25, 8))       # 31
print(toStr(26, 26))      # 10
