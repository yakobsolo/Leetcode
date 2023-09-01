class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , n = 0, len(prices)
        max_profit = 0
        dp = [0] * n
        for r in range(n):
            if prices[l] < prices[r]: dp[r] =  max(dp[r-1], prices[r] -prices[l])
            else: 
                dp[r] = dp[r-1]
                l = r
        return dp[-1]