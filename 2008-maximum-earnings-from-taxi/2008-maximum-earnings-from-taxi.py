class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        N = len(rides)
        dp = [0]*(n+1)
        rides.sort()
        j = N-1
        
        for i in range(n-1, -1, -1):
            
            dp[i]  = dp[i+1]
            
            while j>=0 and rides[j][0] == i:
                s, e, t = rides[j]
                dp[i] = max(dp[i], e-s+t+dp[e])
                j-=1
        
        return dp[1]
                
       