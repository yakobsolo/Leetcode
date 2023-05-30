class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(i, sums):
            
            if i == len(nums):
                if sums == target: return 1
                else: return 0
            
            if (i, sums) not in memo:
                left = dp(i+1, sums+nums[i])
                right = dp(i+1, sums-nums[i])
                
                memo[(i, sums)] = left + right
            return memo[(i, sums)]
        
        return dp(0, 0)