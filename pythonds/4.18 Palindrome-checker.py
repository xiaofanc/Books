"""
dequeue:
A palindrome is a string that reads the same forward and backward, for example, radar, toot, and madam. We would like to construct an algorithm to input a string of characters and check whether it is a palindrome.


"""
from Dequeue import Deque

def palchecker(aString):
    chardeque = Deque()
    match = True

    for ch in aString:
        chardeque.addFront(ch)

    while chardeque.size() > 1 and match:
        first = chardeque.removeFront()
        second = chardeque.removeRear()
        if first != second:
            match = False

    return match

def palchecker(aString):
    return aString == aString[::-1]

if __name__ == '__main__':
    print(palchecker('lsdkjfskf'))
    print(palchecker('radar'))
