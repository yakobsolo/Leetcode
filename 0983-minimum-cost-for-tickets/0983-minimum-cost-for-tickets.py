class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        
        n  = len(days)
        for i in range(n):
            
            dp[i] = inf
            for d, c in zip([1, 7, 30], costs):
                j = i
                
                
                while j >= 0 and days[j] > days[i] - d:
                    j -= 1
                    
                dp[i] = min(dp[i], c+ dp.get(j, 0))
            
        return dp[list(dp)[-1]]                