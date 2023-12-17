class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0 
        N = len(nums)
        l, r = 0, 0
        while r<N:
            if nums[r] -nums[l] >k:
                l = r
                count+=1
            r+=1
        return count+1
                