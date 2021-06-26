class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows = defaultdict(set)
        cols = defaultdict(set)
        m = len(grid)
        n = len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    rows[i].add(j)
                    cols[j].add(i)
        
        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    if len(rows[i]) >= 2 or len(cols[j]) >= 2:
                        ans += 1
        return ans
