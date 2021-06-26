class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        def helper(count, num):
            if nums[num] in self.seen:
                return count
            self.seen.add(nums[num])
            return helper(count+1, nums[num])
        
        res = float('-inf')
        self.seen = set()
        for i in range(len(nums)):
            if not nums[i] in self.seen:
                res = max(res, helper(0, nums[i]))
        return res
