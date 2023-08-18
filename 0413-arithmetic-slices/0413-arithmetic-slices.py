class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        sums = 0
        if n >= 2:
            prev = nums[1] - nums[0]
        dp = [0] * n
        l = 0
        for i in range(2, n):
            cur = nums[i]-nums[i-1]
            if cur == prev:
                dp[i] = 1+ dp[i-1]
                sums+=dp[i]
                
            prev = cur
        return sums
            
            