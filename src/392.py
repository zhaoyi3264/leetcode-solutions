class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        ptr = 0
        for c in t:
            if ptr < len(s) and c == s[ptr]:
                ptr += 1
        return ptr == len(s)
