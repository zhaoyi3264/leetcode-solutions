class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        prev = cost[0]
        cur = cost[1]
        for i in range(2, len(cost)):
            temp = min(prev, cur) + cost[i]
            cur, prev = temp, cur
        return min(prev, cur)
