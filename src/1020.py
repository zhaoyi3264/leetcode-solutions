class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] and (i, j) not in visited:
                visited.add((i, j))
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)
        
        for i in [0, m-1]:
            for j, val in enumerate(grid[i]):
                if val:
                    dfs(i, j)
        for i in range(m):
            for j in [0, n-1]:
                if grid[i][j]:
                    print(i, j)
                    dfs(i, j)
        count = sum(sum(row) for row in grid)
        return count - len(visited)
