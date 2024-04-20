import heapq

class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {1: 0}
        def dfs(n):
            if n in memo:
                return memo[n]
            if n % 2:
                memo[n] = dfs(3 * n + 1) + 1
            else:
                memo[n] = dfs(n // 2) + 1
            return memo[n]
        
        for i in range(lo, hi+1):
            dfs(i)
        l = [(memo[i], i) for i in range(lo, hi+1)]
        heapq.heapify(l)
        for i in range(k):
            ans = heapq.heappop(l)
        return ans[1]
        
