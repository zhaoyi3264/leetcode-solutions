class Solution:
    def getRow(self, row_index: int) -> List[int]:
        prev = []
        for i in range(row_index + 1):
            cur = [None for _ in range(i + 1)]
            cur[0] = cur[-1] = 1
            for j in range(1, i):
                cur[j] = prev[j - 1] + prev[j]
            prev = cur
        return cur
