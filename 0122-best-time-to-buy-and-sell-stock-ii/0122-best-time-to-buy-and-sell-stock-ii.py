class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        profit = 0
        l,r =0,1
        profit1 = 0
        n= len(prices)
        for i in range(1, n):
            if prices[i-1] < prices[i]:
                profit1 += prices[i]-prices[i-1]
            if prices[l] < prices[r]:
                profit = prices[r]-prices[l]
                max_profit = max(profit, max_profit)
            else:
                l=r
            r+=1
        return max(profit1, max_profit)