class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(p, open, close):
            if len(p) == n * 2:
                ans.append(p)
                return
            if open < n:
                dfs(p + '(', open + 1, close)
            if close < open:
                dfs(p + ')', open, close + 1)
        dfs('', 0, 0)
        return ans
