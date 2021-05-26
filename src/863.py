# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if K == 0:
            return [target.val]
        def add_parent(root, parent):
            if not root:
                return
            root.parent = parent
            add_parent(root.left, root)
            add_parent(root.right, root)
        add_parent(root, None)
        
        q = deque([target])
        visited = set()
        step = 0
        while q:
            for _ in range(len(q)):
                n = q.popleft()
                visited.add(n.val)
                if n.left and n.left.val not in visited:
                    q.append(n.left)
                if n.right and n.right.val not in visited:
                    q.append(n.right)
                if n.parent and n.parent.val not in visited:
                    q.append(n.parent)
            step += 1
            if step == K:
                return [n.val for n in q]
        return []
