class Solution:
    def numSquares(self, n: int) -> int:
        
        dp = [n]*(n+1)
        dp[0] = 0
        for i in range(1, n+1):
            for c in range(1,floor(i**0.5)+1):
                dp[i] = min(dp[i], dp[i-(c*c)]+1)
        return dp[n]
        