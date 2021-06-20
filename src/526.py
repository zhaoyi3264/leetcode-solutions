class Solution:
    def countArrangement(self, n: int) -> int:
        self.count = 0
        visited = [0 for _ in range(n+1)]
        def dfs(num):
            if num > n:
                self.count += 1
                return
            for i in range(1, n+1):
                if not visited[i] and ((num % i == 0) or (i % num == 0)):
                    visited[i] = 1
                    dfs(num + 1)
                    visited[i] = 0
        dfs(1)
        return self.count
