"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        tree = {e.id: e for e in employees}
        def dfs(root):
            if not root:
                return 0
            i = root.importance
            for s in root.subordinates:
                i += dfs(tree[s])
            return i
        return dfs(tree[id])
