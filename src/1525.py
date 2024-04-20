class Solution:
    def numSplits(self, s: str) -> int:
        ans = 0
        l = Counter()
        r = Counter(s)
        for c in s:
            l[c] += 1
            r[c] -= 1
            if r[c] == 0:
                del r[c]
            if len(l) == len(r):
                ans += 1
        return ans
