class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def palindrome(start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        
        ans = []
        def dfs(start, path):
            if start >= len(s):
                ans.append(path)
            for l in range(len(s) - start):
                if palindrome(start, start + l):
                    dfs(start + l + 1, path + [s[start:start+l+1]])
        dfs(0, [])
        return ans
