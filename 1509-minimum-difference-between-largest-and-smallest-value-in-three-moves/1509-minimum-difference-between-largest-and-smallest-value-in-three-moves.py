class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums)<5: return 0
        n = len(nums)
        nums.sort()
        return min(nums[-4] -  nums[0], nums[n-1] - nums[3], nums[-3] - nums[1], nums[-2]- nums[2])