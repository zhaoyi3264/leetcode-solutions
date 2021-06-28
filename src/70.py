# from functools import lru_cache

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        prev = 1
        cur = 2
        for i in range(2, n):
            cur, prev = cur + prev, cur
        return cur
