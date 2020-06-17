"""
Our second method to represent a tree uses nodes and references. In this case we will define a class that has attributes for the root value, as well as the left and right subtrees. 

"""

class BinaryTree:
    # the root object of a tree can be a reference to any object
    def __init__(self, rootobj):
        self.root = rootobj
        self.left = None
        self.right = None

    def insertLeft(self, newnode):
        if self.left == None:
            self.left = BinaryTree(newnode)
        else: # node with an existing left child.
            t = BinaryTree(newnode)
            t.left = self.left
            self.left = t

    def insertRight(self, newnode):
        if self.right == None:
            self.right = BinaryTree(newnode)
        else:
            t = BinaryTree(newnode)
            t.left = self.left
            self.left = t

    def getRoot(self):
        return self.root

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def setRoot(self, obj):
        self.root = obj

    def preorder(self):
        print(self.root)
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def __repr__(self):
        return 'N(%s, L%s, R%s)' % (self.root, self.left or '', self.right or '')

if __name__ == '__main__':
 
    r = BinaryTree('a')
    r.insertLeft('b')
    r.insertRight('c')
    r.getLeft().insertRight('d')
    r.getRight().insertLeft('e')
    r.getRight().insertRight('f')
    print(r)
    print(r.preorder())




        