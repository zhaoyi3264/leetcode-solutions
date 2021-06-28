class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_sum = 0
        max_sum = nums[0]
        sum = 0
        for num in nums:
            sum += num
            max_sum = max(max_sum, sum - min_sum)
            min_sum = min(min_sum, sum)
        return max_sum
