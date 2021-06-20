class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        n = len(needs)
        def dfs(needs):
            ans = 0
            for i in range(n):
                ans += needs[i] * price[i]
            
            for s in special:
                needs_copy = needs.copy()
                valid = True
                for i in range(n):
                    if needs_copy[i] < s[i]:
                        valid = False
                        break
                    needs_copy[i] -= s[i]
                if valid:
                    ans = min(ans, dfs(needs_copy) + s[-1])
            return ans
        return dfs(needs)
