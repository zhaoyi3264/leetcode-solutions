class Solution:
    def fib(self, n: int) -> int:
        prev, cur = 0, 1
        if n == 0:
            return prev
        if n == 1:
            return cur
        for i in range(n):
            prev, cur = cur, prev + cur
        return prev
