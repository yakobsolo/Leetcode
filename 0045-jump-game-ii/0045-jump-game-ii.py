class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0]*N
        for i in range(N-1):
            
            for j in range(1, nums[i]+1):
                if i + j == N-1:
                    return dp[i]+1
                if dp[i+j] == 0:
                    dp[i+j] = dp[i]+1
                else:
                    dp[i+j] = min(dp[i+j], dp[i] + 1)
                    
        return 0