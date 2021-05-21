class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        ans = []
        while label > 0:
            ans.append(label)
            label //= 2
        res = []
        n = len(ans) - 1
        for i, a in enumerate(ans):
            if i % 2 == 1:
                res.append(2**(n-i) + 2**(n-i+1) - a - 1)
            else:
                res.append(a)
        return reversed(res)
