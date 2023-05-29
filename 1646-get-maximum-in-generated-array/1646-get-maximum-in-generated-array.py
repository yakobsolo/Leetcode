class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n<2: return n
        dp = [0]*(n+1)
        
        dp[1] = 1
        ptr, ans = 1, 0
        for i in range(2, n+1):
            
            if i%2 == 0: dp[i] = dp[i//2]
            else:
                dp[i] = dp[ptr] + dp[ptr+1]
                ptr +=1
            ans = max(ans, dp[i])
        return ans