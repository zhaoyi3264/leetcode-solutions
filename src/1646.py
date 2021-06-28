class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n < 2:
            return n
        ans = [None for _ in range(n + 1)]
        ans[0] = 0
        ans[1] = 1
        for i in range(1, n // 2 + 1):
            ans[2 * i] = ans[i]
            if 2 * i + 1 < n + 1:
                ans[2 * i + 1] = ans[i] + ans[i + 1]
        return max(ans)
