class Solution:
    def tribonacci(self, n: int) -> int:
        n_0 = 0
        n_1 = 1
        n_2 = 1
        for i in range(n):
            n_3 = n_0 + n_1 + n_2
            n_2, n_1, n_0 = n_3, n_2, n_1
        return n_0
