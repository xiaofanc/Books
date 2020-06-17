"""
binary search tree:

Map() Create a new, empty map.
put(key,val) Add a new key-value pair to the map. If the key is already in the map then replace the old value with the new value.
get(key) Given a key, return the value stored in the map or None otherwise.
del Delete the key-value pair from the map using a statement of the form del map[key].
len() Return the number of key-value pairs stored in the map.
in Return True for a statement of the form key in map, if the given key is in the map.

"""
class TreeNode:
    def __init__(self,key,val,left=None,right=None,
                                       parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

    # for two children case
    # find the next-largest key of the currentnode
    # The successor is guaranteed to have no more than one child, so we know how to remove it using the two cases for deletion that we have already implemented. Once the successor has been removed, we simply put it in the tree in place of the node to be deleted.
    # There are three cases to consider when looking for the successor:
    # If the node has a right child, then the successor is the smallest key in the right subtree.
    # If the node has no right child and is the left child of its parent, then the parent is the successor.
    # If the node has no right child and is the right child of its parent, then the successor of the node is the successor of the parent excluding the node.

    def findSuccessor(self):
        if self.hasRightChild(): # only this case matters for BST
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.leftChild
        return current

    # The reason we use spliceOut is that it goes directly to the node we want to splice out and makes the right changes. We could call delete recursively, but then we would waste time re-searching for the key node.
    def spliceOut(self):
        # remove succ
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        # succ has one child
        if self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent  
            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent

    def __repr__(self):
        return 'N(%s, L%s, R%s)' % (self.root, self.leftChild or '', self.rightChild or '')

class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    # insert method
    # This method will check to see if the tree already has a root. If there is not a root then put will create a new TreeNode and install it as the root of the tree. If a root node is already in place then put calls the private, recursive, helper function _put to find the right position
    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            # go to the left subtree
            if currentNode.hasLeftChild():
                self._put(key, val, currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key, val)
        else: # fo the right subtree
            if currentNode.hasRightChild():
                self._put(key, val, currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key, val)

    # This allows us to write Python statements like myZipTree['Plymouth'] = 55446
    def __setitem__(self, k, v):
        self.put(k,v)

    # get method
    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None

    # serch until find or None
    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif key < currentNode.key:
            self._get(key, currentNode.leftChild)
        elif key > currentNode.key:
            self._get(key, currentNode.rightChild)
        else: # key == currentNode.key:
            return currentNode
    # accessing a dictionary
    def __getitem__(self, key):
        return self.get(key)

    # in method
    def __contains__(self, key):
        if self.get(key): 
            return True
        else:
            return False

    # delete method
    # deelte the key if found, else raise an error
    def delete(self, key):
        # if more than one node
        if self.size > 1:
            nodetodelete = self._get(key, self.node)
            # found
            if nodetodelete:
                self.remove(nodetodelete)
                self.size -= 1
            # not found
            else:
                raise KeyError('key is not in the tree')
        # if delete the root
        elif self.size == 1 and key == self.root.key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError('key is not in the tree')

    def __delitem__(self, key):
        return self.delete(key)

    # Once we’ve found the node containing the key we want to delete, there are three cases that we must consider:
    # The node to be deleted has no children 
    # The node to be deleted has only one child
    # The node to be deleted has two children
    def remove(self, currentNode):
        # none children
        # delete the node and remove the reference to this node in the parent.
        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        # two children
        elif currentNode.hasBothChildren():
            # find the next largest node
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.key = succ.key 
            currentNode.payload = succ.payload

        else:
            # if currentnode has leftchild
            if currentNode.hasLeftChild():
                # if current is leftchild, change reference for parent
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                # if current is rightchild, change reference for parent 
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                # # if currentnode is root, replace currentnode with leftchild
                else: 
                    currentnode.replaceNodeData(currentnode.leftChild.key, currentnode.leftChild.payload, currentnode.leftChild.leftChild, currentnode.leftChild,rightChild)

            if currentNode.hasRightChild():
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.rightChild
                else: 
                    currentnode.replaceNodeData(currentnode.rightChild.key, currentnode.rightChild.payload, currentnode.rightChild.leftChild, currentnode.rightChild,rightChild)


    # yield also takes the additional step of freezing the state of the function so that the next time the function is called it continues executing from the exact point it left off earlier. 
    # inorder iterator - generator functions
    def __iter__(self):
        if self:
            if self.hasLeftChild():
                for elem in self.leftChiLd:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.rightChild:
                    yield elem






mytree = BinarySearchTree()
mytree[3]="red"
mytree[4]="blue"
mytree[6]="yellow"
mytree[2]="at"
print(mytree.root)

print(mytree[6])
print(mytree[2])

























