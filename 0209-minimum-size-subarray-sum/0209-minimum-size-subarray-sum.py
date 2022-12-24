class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        long, min_long = len(nums),len(nums)
        sums = 0
        l = 0
        if sum(nums) < target:
            return 0
        for i in range(len(nums)):
            sums +=nums[i]
            while sums>= target:
                long = i-l+1
                min_long = min(min_long, long)
                sums-= nums[l]
                l+=1
        return min_long
                