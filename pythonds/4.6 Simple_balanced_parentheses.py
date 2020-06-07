"""
Stack:
(5+6)*(7+8)/(4+3)
"""
# Solution 1:
from Stack import Stack

def parChecker(par):
    s = Stack()
    balanced = True
    i = 0
    while i < len(par) and balanced:
        if par[i] == "(":
            s.push(par[i])
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        i += 1

    return balanced and s.isEmpty()

print('((()))', parChecker('((()))'))
print('((())', parChecker('((())'))

# A general case: { { ( [ ] [ ] ) } ( ) }
# solution 1:
def parChecker(par):
    s = Stack()
    balanced = True
    i = 0
    par_dct = {'(':')', '{':'}', '[':']'}
    while i < len(par) and balanced:
        # print(par, s)
        if par[i] in par_dct:
            s.push(par[i])
        elif (not s.isEmpty()) and par_dct[s.peek()] == par[i]:
            s.pop()
        else:
            balanced = False

        i += 1

    return balanced and s.isEmpty()

print('{(())}', parChecker("{(())}"))
print('[(()]', parChecker("[(()]"))

# solution 2:
def parChecker2(par):
    stack = []
    par_dct = {'(':')', '{':'}', '[':']'}

    for i in range(len(par)):
        if par[i] in par_dct:
            stack.append(par[i])
        elif stack and par[i] == par_dct[stack[-1]]:
            stack.pop()
        else:
            return False

    return stack == []

print('{(())}', parChecker2("{(())}"))
print('[(()]', parChecker2("[(()]"))

