class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        expense = -prices[0]
        profit = 0
        
        n = len(prices)
        for i in range(1, n):
            expense = max(expense, profit - prices[i])
            profit =  max(profit, expense+prices[i]-fee)
        return profit
        