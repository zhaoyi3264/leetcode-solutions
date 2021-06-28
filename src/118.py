class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        ans = []
        for i in range(num_rows):
            row = [None for _ in range(i + 1)]
            row[0], row[-1] = 1, 1
            for j in range(1, i):
                row[j] = ans[i - 1][j - 1] + ans[i - 1][j]
            ans.append(row)
        return ans
