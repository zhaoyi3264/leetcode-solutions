class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i, j):
            grid[i][j] = -1
            sides = 0
            offsets = [0, -1, 0, 1, 0]
            for off in range(4):
                p, q = i + offsets[off], j + offsets[off + 1]
                if 0 <= p < m and 0 <= q < n:
                    if grid[p][q] == 0:
                        sides += 1
                    elif grid[p][q] == 1:
                        dfs(p, q)
                else:
                    sides += 1
            self.ans += sides
        self.ans = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j)    
                    return self.ans
