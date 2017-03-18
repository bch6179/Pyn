def swap(t1, t2):
    return t2, t1
    
class ListNode:
    def __init__(self, val, tnext=None):
        self.val = val
        self.next = tnext
    def __repr__(self):
        return """ListNode(val=%r, next=%r""" % (self.val, self.next)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = tnext
    def __repr__(self):
        return """TreeNode(val=%r, left=%r, right=%r""" % (self.val, self.left, self.right)
class TreeNode:
    def __init__(self, val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return """TreeNode(val=%r, left=%r, right=%r""" % (self.val, self.left, self.right)
class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if(self.root == None):
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if(val < node.v):
            if(node.l != None):
                self._add(val, node.l)
            else:
                node.l = Node(val)
        else:
            if(node.r != None):
                self._add(val, node.r)
            else:
                node.r = Node(val)

    def find(self, val):
        if(self.root != None):
            return self._find(val, self.root)
        else:
            return None

    def _find(self, val, node):
        if(val == node.v):
            return node
        elif(val < node.v and node.l != None):
            self._find(val, node.l)
        elif(val > node.v and node.r != None):
            self._find(val, node.r)

    def deleteTree(self):
        # garbage collector will do this for us. 
        self.root = None

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            print str(node.v) + ' '
            self._printTree(node.r)

#     3
# 0     4
#   2      8
# tree = Tree()
# tree.add(3)
# tree.add(4)
# tree.add(0)
# tree.add(8)
# tree.add(2)
# tree.printTree()
# print (tree.find(3)).v
# print tree.find(10)
# tree.deleteTree()
# tree.printTree()