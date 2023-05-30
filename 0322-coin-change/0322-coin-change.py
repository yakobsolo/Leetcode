class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        t = amount +1
        dp = [t] * t
        dp[0] = 0
        for i in range(1, t):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
        return dp[t-1] if dp[t-1] != t else -1
                    
            
            