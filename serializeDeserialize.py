https://leetcode.com/problems/serialize-and-deserialize-bst/?tab=Description


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
         
        def dfs(root):     
            if not root: return '#'
            res =  str(root.val) + ','+dfs(root.left) + ','+dfs(root.right)
            return res
            
            
        return dfs(root)
    def __init__(self):
        self.index = 0
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(src):
            
            if self.index >= len(src) or src[self.index] == '#': 
                self.index+=1
                return None
            cur = TreeNode(int(src[self.index]))
            self.index += 1
            cur.left = dfs(src)
            cur.right = dfs(src)
            return cur
        src = data.split(',')
        return dfs(src)
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
         
        def dfs(root):     
            if not root: return '#'
            res =  str(root.val) + ','+dfs(root.left) + ','+dfs(root.right)
            return res
            
            
        return dfs(root)
    def __init__(self):
        self.index = 0
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def dfs(data):
         
            len(data) or data[self.index] == '#': 
                self.index+=2
                return None
            cur = TreeNode(data[self.index])
            self.index += 2
            cur.left = dfs(data)
            cur.right = dfs(data)
            return cur
        return dfs(data)
from base import *
# Your Codec object will be instantiated and called as such:
codec = Codec()
root = TreeNode(0, left=TreeNode(1, right=TreeNode(5)))

root1 = TreeNode(0, left=TreeNode(1, right=TreeNode(5)), right=TreeNode(2))
print codec.serialize(root)
print codec.deserialize(codec.serialize(root))

class Codec:
    
    def serialize(self, root):
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')
        vals = []
        doit(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()

class Codec:
    
    def serialize(self, root):
        code, queue = "", [root]
        for node in queue:
            code += "," * (node != root) + "#" * (not node) + (str(node.val) if node else "")
            if node: queue += node.left, node.right,
        return code
        
        
    def deserialize(self, data):
        data = collections.deque(data.split(","))
        val = data.popleft()
        root = TreeNode(int(val)) if val != "#" else None
        queue = [root]
        for node in queue:
            if not node: continue
            l, r = data.popleft(), data.popleft()
            node.left  = TreeNode(int(l)) if l != "#"  else None
            node.right = TreeNode(int(r)) if r != "#" else None
            queue += node.left, node.right,
        return root   

        def serialize(self, root):
        preorder = ''
    if not root:
        preorder += ',None'
        return preorder
    preorder += ','+str(root.val)
    preorder += self.serialize(root.left)
    preorder += self.serialize(root.right)
    return preorder

def deserialize(self, encode_data):
    pos = -1
    data = encode_data[1:].split(',')
    for i in xrange(len(data)):
        if data[i] == 'None':
            data[i] = None
        else:
            data[i] = int(data[i])
    root, count = self.buildTree(data, pos)
    return root
    
def buildTree(self, data, pos):
    pos += 1
    if pos >= len(data) or data[pos]==None:
        return None, pos
        
    root = TreeNode(data[pos])
    root.left, pos = self.buildTree(data, pos)
    root.right, pos = self.buildTree(data, pos)
    return root, pos     