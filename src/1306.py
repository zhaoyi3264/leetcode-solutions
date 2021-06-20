class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        def dfs(i):
            if arr[i] == 0:
                return True
            if i in visited:
                return 
            visited.add(i)
            left, right = False, False
            if i - arr[i] >= 0:
                left = dfs(i - arr[i])
            if i + arr[i] < n:
                right = dfs(i + arr[i])
            return left or right
        return dfs(start)
