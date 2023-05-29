class Solution:
    
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[0]
        second = cost[1]
        
        n = len(cost)
        for i in range(2, n):
            temp  = min(first, second) + cost[i]
            first = second
            second = temp
        return min(first, second)
            