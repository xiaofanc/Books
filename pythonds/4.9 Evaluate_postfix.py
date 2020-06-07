"""
Stack:
Consider the postfix expression 4 5 6 * +. As you scan the expression from left to right, you first encounter the operands 4 and 5. At this point, you are still unsure what to do with them until you see the next symbol. Placing each on the stack ensures that they are available if an operator comes next.

In this case, the next symbol is another operand. So, as before, push it and check the next symbol. Now we see an operator, *. This means that the two most recent operands need to be used in a multiplication operation. By popping the stack twice, we can get the proper operands and then perform the multiplication (in this case getting the result 30).

We can now handle this result by placing it back on the stack so that it can be used as an operand for the later operators in the expression. When the final operator is processed, there will be only one value left on the stack. Pop and return it as the result of the expression. 

Assume the postfix expression is a string of tokens delimited by spaces. 
The operators are *, /, +, and - and the operands are assumed to be single-digit integer values. The output will be an integer result.

- Create an empty stack called operandStack.
- Convert the string to a list by using the string method split.
- Scan the token list from left to right.

    a. If the token is an operand, convert it from a string to an integer and push the value onto the operandStack.
    b. If the token is an operator, *, /, +, or -, it will need two operands. Pop the operandStack twice. The first pop is the second operand and the second pop is the first operand. Perform the arithmetic operation. Push the result back on the operandStack.

- When the input expression has been completely processed, the result is on the stack. Pop the operandStack and return the value.


opstack = 4 5 6
pop 5,6   5*6 = 30, push it back
opstack = 4 30 
pop 4,30  4+30 = 34, push it back


"""
from Stack import Stack

def postfixEval(postfixexpr):
    tokenlist = postfixexpr.split()
    opstack = Stack()

    for token in tokenlist:
        if token.isnumeric():
            opstack.push(token)
        else: # token is an operator, *, /, +, or -
            operand_2 = int(opstack.pop())
            operand_1 = int(opstack.pop())
            res = domath(operand_1, operand_2, token)
            opstack.push(res)

    return opstack.pop()

def domath(num1, num2, token):
    if token == "+":
        return num1 + num2
    elif token == "-":
        return num1 - num2
    elif token == "*":
        return num1 * num2
    else:
        return num1 / num2

print(postfixEval("4 5 6 * +") == 34)
print(postfixEval('7 8 + 3 2 + /') == 3)
print(postfixEval('17 10 + 3 * 9 /') == 9)



