# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return None
        res = []
        q = deque([root])
        while q:
            n = q.popleft()
            res.append(str(n.val) if n else '-')
            if n is not None:
                q.append(n.left)
                q.append(n.right)
        return ' '.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        vals = data.split(' ')
        temp = root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q:
            n = q.popleft()
            if vals[i] != '-':
                n.left = TreeNode(vals[i])
                q.append(n.left)
            i += 1
            if vals[i] != '-':
                n.right = TreeNode(vals[i])
                q.append(n.right)
            i += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
