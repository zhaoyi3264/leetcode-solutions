class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ans = 0
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] and (i, j) not in visited:
                visited.add((i, j))
                return 1 + dfs(i-1, j) + dfs(i+1, j) + dfs(i, j-1) + dfs(i, j+1)
            return 0
        
        for i in range(len(grid)):
            for j, val in enumerate(grid[i]):
                if val and (i, j) not in visited:
                    ans = max(ans, dfs(i, j))
        return ans
