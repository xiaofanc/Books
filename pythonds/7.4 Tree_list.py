"""
In a list of lists tree, we will store the value of the root node as the first element of the list. The second element of the list will itself be a list that represents the left subtree. The third element of the list will be another list that represents the right subtree.


"""

# myTree = ['a', ['b', ['d',[],[]], ['e',[],[]] ], ['c', ['f',[],[]], []] ]
# print(myTree)
# print('left subtree = ', myTree[1])
# print('root = ', myTree[0])
# print('right subtree = ', myTree[2])

def BinaryTree(r):
    return [r, [], []]

def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1: # already have left node
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])

def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1: # already have left node
        root.insert(2, [newBranch, t, []])
    else:
        root.insert(2, [newBranch, [], []])

def getRootVal(root):
    return root[0]

def setRootVal(root,newVal):
    root[0] = newVal

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

r = BinaryTree(3)
insertLeft(r,4)
insertLeft(r,5)
insertRight(r,6)
insertRight(r,7)
print(r)
print(getLeftChild(r))
print(getRightChild(r))
l = getLeftChild(r)

setRootVal(l, 9)
print(r)
insertLeft(l, 11)
print(r)
print(getLeftChild(getRightChild(r)))

r = BinaryTree('a')
insertLeft(r,'b')
insertRight(r,'c')
insertRight(getLeftChild(r),'d')
insertLeft(getRightChild(r),'e')
insertRight(getRightChild(r),'f')
print(r)




