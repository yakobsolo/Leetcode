class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        
        n  = len(days)
        for i in range(n-1, -1, -1):
        
        
            
            dp[i] = inf
            for d, c in zip([1, 7, 30], costs):
                j = i
                
                while j < n and days[j] < days[i] + d:
                    j +=1
                    
                dp[i] = min(dp[i], c+ dp.get(j, 0))
            
        return dp[0]
                