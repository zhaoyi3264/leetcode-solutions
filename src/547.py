class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        count = 0
        def dfs(root):
            if root in visited:
                return
            visited.add(root)
            for child, connected in enumerate(isConnected[root]):
                if connected:
                    dfs(child)
        for i in range(len(isConnected)):
            if i not in visited:
                count += 1
                dfs(i)
        return count
