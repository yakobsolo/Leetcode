class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo1 = {}
        memo2 = {}
        def dp1(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[0], nums[1])
            
            if i not in memo1:
                memo1[i] = max(dp1(i-1), dp1(i-2) + nums[i])
            return memo1[i]
        def dp2(i):
            if i == 1:
                return nums[i]
            if i == 2:
                return max(nums[1], nums[2])
            
            if i not in memo2:
                memo2[i] = max(dp2(i-1), dp2(i-2) + nums[i])
            return memo2[i]
        n = len(nums)
        if n<2: return nums[0]
        return max(dp1(n-2), dp2(n-1))