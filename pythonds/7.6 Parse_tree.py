"""
Parse trees can be used to represent real-world constructions like sentences or mathematical expressions.

- How to build a parse tree from a fully parenthesized mathematical expression.
- How to evaluate the expression stored in a parse tree.
- How to recover the original mathematical expression from a parse tree.

Rule:
1. If the current token is a '(', add a new node as the left child of the current node, and descend to the left child (currentTree).
2. If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator represented by the current token. Add a new node as the right child of the current node and descend to the right child (currentTree).
3. If the current token is a number, set the root value of the current node to the number and return to the parent (pop stack).
4. If the current token is a ')', go to the parent of the current node.

# ( 3 + ( 4 * 5 ) )
['(', '3', '+', '(', '4', '*', '5' ,')',')']

how can we keep track of the parent?
A simple solution to keeping track of parents as we traverse the tree is to use a stack. Whenever we want to descend to a child of the current node, we first push the current node on the stack. When we want to return to the parent of the current node, we pop the parent off the stack.

currentTree is a shallow copy of pTree, which will change the object in the stack too!!

"""
from Stack import Stack
from Treenodes import BinaryTree

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    pTree = BinaryTree('')
    pStack.push(pTree) # pStack [N(, L, R)]
    currentTree = pTree
    print("fplist", fplist, "pTree", pTree, "pStack", pStack, "currentTree", currentTree)

    for i in fplist:
        # 1. add a new node as the left child of the current node, and descend to the left child.
        print("i", i)
        if i == "(":
            currentTree.insertLeft('')
            # 1st '(' pStack [N(, LN(, L, R), R), N(, LN(, L, R), R)]
            # the first object changed!
            # 2d '(' pStack [N(, LN(, L, R), R), 
                    # N(+, LN(3, L, R), RN(, LN(, L, R), R)), 
                    # N(+, LN(3, L, R), RN(, LN(, L, R), R))] 
            pStack.push(currentTree)
            currentTree = currentTree.getLeft()
            print("pTree", pTree, "pStack", pStack, "currentTree", currentTree)
        # set the root value of the current node to the operator represented by the current token. Add a new node as the right child of the current node and descend to the right child.
        elif i in ['+','-','*','/']:
            currentTree.setRoot(i)
            currentTree.insertRight('')
            # + pStack [N(+, LN(3, L, R), RN(, L, R)), 
                      # N(+, LN(3, L, R), RN(, L, R))]
            pStack.push(currentTree)
            currentTree = currentTree.getRight()
            # + currentTree N(, L, R)
            print("pTree", pTree, "pStack", pStack, "currentTree", currentTree)

        # go to the parent of the current node.
        elif i == ")":
            currentTree = pStack.pop()
            print("pTree", pTree, "pStack", pStack, "currentTree", currentTree)

        # set the root value of the current node to the number and return to the parent.
        else:
            try:
                currentTree.setRoot(int(i))
                parent = pStack.pop()
                # 3: pStack [N(, LN(3, L, R), R)]
                currentTree = parent
                # 3: currentTree N(, LN(3, L, R), R)
            except ValueError:
                raise ValueError(f"token {i} is not a valid integer")
            print("pTree", pTree, "pStack", pStack, "currentTree", currentTree)

    return pTree


print(buildParseTree("( 3 + ( 4 * 5 ) )"))











