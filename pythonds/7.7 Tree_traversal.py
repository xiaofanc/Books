"""
preorder, inorder, postorder

"""

def preorder(tree):
    if tree:
        print(tree.getRoot())
        preorder(tree.getLeft())
        preorder(tree.getRight())

def postorder(tree):
    if tree:
        preorder(tree.getLeft())
        preorder(tree.getRight())
        print(tree.getRoot())

def inorder(tree):
    if tree:
        preorder(tree.getLeft())
        print(tree.getRoot())
        preorder(tree.getRight())



        


