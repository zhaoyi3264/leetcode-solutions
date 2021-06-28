class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = nums[0]
        for n in nums[1:]:
            if not steps:
                return False
            steps -= 1
            steps = max(steps, n)
        return True
