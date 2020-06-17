"""
First, we obtain references to the left and the right children of the current node. If both the left and right children evaluate to None, then we know that the current node is really a leaf node. 

If the current node is not a leaf node, look up the operator in the current node and apply it to the results from recursively evaluating the left and right children.

When we look up an operator in the dictionary, the corresponding function object is retrieved. Since the retrieved object is a function, we can call it in the usual way function(param1,param2). So the lookup opers['+'](2,2) is equivalent to operator.add(2,2).

"""
from Treenodes import BinaryTree
import operator

def evaluate(parseTree):
    opers = {"+": operator.add, "-": operator.sub, "*":operator.mul, "/":operator.truediv}

    leftc = parseTree.getLeft()
    rightc = parseTree.getRight()

    # base
    if leftc == None and rightc == None:
        return parseTree.getRoot()  # number
    else:
        fn = opers[parseTree.getRoot()]
        return fn(evaluate(leftc), evaluate(rightc))

# Let’s rewrite the evaluation function, but model it even more closely on the postorder code for parse tree
def postordereval(parsetree):
    opers = {"+": operator.add, "-": operator.sub, "*":operator.mul, "/":operator.truediv}
    left = None
    right = None
    if parsetree:
        left = postordereval(parsetree.getLeft())
        right = postordereval(parsetree.getRight())
        print(left, right)

        if left and right:
            return opers[parsetree.getRoot()](left, right)
        else:
            return parsetree.getRoot()

def printexp(exptree):
    sval = ""
    if exptree == None:
        return ''
    if exptree.getLeft() == None and exptree.getRight() == None:
        return str(exptree.getRoot())
    else:
        sval = sval + '(' + printexp(exptree.getLeft()) + str(exptree.getRoot()) + printexp(exptree.getRight()) + ')'
    return sval

r = BinaryTree('+')
r.insertLeft(3)
r.insertRight('*')
r.getRight().insertLeft(4)
r.getRight().insertRight(5)
print(r)

# print(evaluate(r))  # 23
"""
   + 
 4    /
     3   2  
"""
r = BinaryTree('+')
r.insertLeft(4)
r.insertRight('/')
r.getRight().insertLeft(3)
r.getRight().insertRight(2)
print(r)

# print(evaluate(r))  # 4.5
print(postordereval(r))  # 5.5

print(printexp(r))

