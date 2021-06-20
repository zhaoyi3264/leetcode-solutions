class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        t = defaultdict(set)
        for i, m in enumerate(manager):
            if m >= 0:
                t[m].add(i)
        def dfs(root):
            time = 0
            for child in t[root]:
                time = max(time, dfs(child))
            return time + informTime[root]
        return dfs(headID)
