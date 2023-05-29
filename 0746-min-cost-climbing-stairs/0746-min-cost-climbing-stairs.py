class Solution:
    
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        min_cost = 0
        cost.append(0)
        n = len(cost)
        def dp(i):
            nonlocal min_cost
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]
            
            if i not in memo: 
                memo[i] = min(dp(i-1), dp(i-2)) + cost[i]
                
            return memo[i]
        return dp(n-1)
            