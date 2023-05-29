class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1: return nums[0]
        def dp(l,r):
            if r < l: return 0
            if l == r:return nums[l]
            if r not in memo:
                memo[r] = max(dp(l,r-1),dp(l,r-2)+nums[r])
            return memo[r]
        memo = {}
        n= len(nums)
        res =dp(1, n-1)
        memo = {}
        res = max(res,dp(0,n-2))
        return res
    
    
    