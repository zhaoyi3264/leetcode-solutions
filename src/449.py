# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        ans = f'{root.val:x}'
        if not root.left and not root.right:
            return ans
        else:
            return ans + f',{self.serialize(root.left)},{self.serialize(root.right)}'

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def dec(data):
            if not data:
                return None
            root = TreeNode(data[0]) if data[0] is not None else None
            if len(data) == 1:
                return root
            for i, v in enumerate(data):
                if v and v > data[0]:
                    break
            root.left = dec(data[1:i])
            root.right = dec(data[i:])
            return root
        if not data:
            return None
        data = [(int(d, 16) if d else None) for d in data.split(',')]
        return dec(data)

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
