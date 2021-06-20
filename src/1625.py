class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        digit = list(s)
        visited = set()
        def dfs(digit):
            d_a = digit.copy()
            for i, d in enumerate(digit):
                if i % 2:
                    d_a[i] = str((int(d_a[i]) + a) % 10)
            str_a = ''.join(d_a)
            if str_a not in visited:
                visited.add(str_a)
                dfs(d_a)
            
            d_b = digit[-b:] + digit[:-b]
            str_b = ''.join(d_b)
            if str_b not in visited:
                visited.add(str_b)
                dfs(d_b)
            
        dfs(digit)
        return min(visited)
