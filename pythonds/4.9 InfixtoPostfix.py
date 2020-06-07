"""
Stack:
Conversion of Infix Expressions to Prefix and Postfix¶

if fully parenthesized infix:
prefix: moving the symbol to the position of the left matching parenthesis
postfix: moving the symbol to the position of the right matching parenthesis

(A + B) * C Recall that A B + C * is the postfix equivalent. 
In this case, when we see *, + has already been placed in the result expression because it has precedence over * by virtue of the parentheses. 
When that right parenthesis does appear, the operator + can be popped from the stack.

Assume the infix expression is a string of tokens delimited by spaces. 
The operator tokens are *, /, +, and -, along with the left and right parentheses, ( and ). 
The operand tokens are the single-character identifiers A, B, C, and so on. 
The following steps will produce a string of tokens in postfix order.

- Create an empty stack called opstack for keeping operators. Create an empty list for output.
- Convert the input infix string to a list by using the string method split.
- Scan the token list from left to right.

    a. If the token is an operand, append it to the end of the output list.
    b. If the token is a left parenthesis, push it on the opstack.
    c. If the token is a right parenthesis, pop the opstack until the corresponding left parenthesis is removed. Append each operator to the end of the output list.
    d. If the token is an operator, *, /, +, or -, push it on the opstack. However, first remove any operators already on the opstack that have higher or equal precedence and append them to the output list.

- When the input expression has been completely processed, check the opstack. Any operators still on the stack can be removed and appended to the end of the output list.

# ( A + B ) * C - ( D - E ) * ( F + G )
# opStack = ( +
# output  = A B 

# opStack = 
# output  = A B +

# opStack = *
# output  = A B + C 

# opStack = -
# output  = A B + C *

# opStack = - (
# output  = A B + C * 

# opStack = - ( -
# output  = A B + C * D E

# opStack = - 
# output  = A B + C * D E -

# opStack = - * (
# output  = A B + C * D E - F

# opStack = - * ( + 
# output  = A B + C * D E - F G

# opStack = - * 
# output  = A B + C * D E - F G +

# opStack = 
# output  = A B + C * D E - F G + * -

"""

from Stack import Stack
import re

def infixToPostfix(infixexpr):
    prec = {'**': 4, '*':3, '/':3, '+':2, '-':2, '(':1}
    opStack = Stack() # to store +-*/(
    postfixList = []  # output
    tokenlist = infixexpr.split()   # split string
    # print(tokenlist)

    for token in tokenlist:
        # a: append to the output 
        # pattern = re.compile("[A-Za-z0-9]+")
        # if pattern.fullmatch(token):
        if token.isalnum():  
            postfixList.append(token)
        # b: push (
        elif token == '(':
            opStack.push(token)
        # c: pop until matching ( 
        elif token == ')':
            toptoken = opStack.pop()
            while toptoken != '(':
                postfixList.append(toptoken)
                toptoken = opStack.pop()
        else: # token is an operator, *, /, +, or -
            while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return " ".join(postfixList)

print(infixToPostfix("A * B + C * D") == "A B * C D * +") 
print(infixToPostfix("( A + B ) * C - ( D - E ) * ( F + G )") == "A B + C * D E - F G + * -")

print(infixToPostfix("( A + B ) * ( C + D )") == 'A B + C D + *')
print(infixToPostfix("( A + B ) * C") == 'A B + C *')
print(infixToPostfix("A + B * C") == 'A B C * +')

print(infixToPostfix("10 + 3 * 5 / ( 16 - 4 )") == '10 3 5 * 16 4 - / +')
print(infixToPostfix("5 * 3 ** ( 4 - 2 )"))




