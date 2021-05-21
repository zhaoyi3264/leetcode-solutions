# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorder(self, root):
        if not root:
            return []
        l = []
        l.extend(self.inorder(root.left))
        l.append(root.val)
        l.extend(self.inorder(root.right))
        return l
    
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l1 = self.inorder(root1)
        l2 = self.inorder(root2)
        p1 = 0
        p2 = 0
        l = []
        while True:
            b1 = p1 < len(l1)
            b2 = p2 < len(l2)
            if b1 and b2:
                if l1[p1] < l2[p2]:
                    l.append(l1[p1])
                    p1 += 1
                else:
                    l.append(l2[p2])
                    p2 += 1
            elif b1:
                l.append(l1[p1])
                p1 += 1
            elif b2:
                l.append(l2[p2])
                p2 += 1
            else:
                break
        return l
