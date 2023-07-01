class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n>2:
            dp = [0]*n
            dp[0], dp[1] = nums[0], max(nums[1], nums[0])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            return dp[n-1]
            
        elif n==2: return max(nums[0], nums[1])
        else: return nums[0]