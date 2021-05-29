class Solution:
    def numTrees(self, n: int) -> int:
        """
        trees(n) = sum(dp(n-1)*dp(1) + dp(n-2)*dp(2) + ...)
        [1, 1, 2, 5, ...]
        """
        if n < 2:
            return 1
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        for nodes in range(2, n + 1):
            for left in range(nodes):
                dp[nodes] += dp[left] * dp[nodes - 1 - left]
        return dp[-1]
