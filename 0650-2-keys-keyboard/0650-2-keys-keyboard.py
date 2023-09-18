class Solution:
    def minSteps(self, n: int) -> int:
        dp = [0]*(n+1)
        
        for i in range(2, n+1):
            
            if i %2 == 0:
                dp[i] = dp[i//2] +2
            else:
                j = i//2
                while i%j != 0:
                    j-=1
                dp[i] = dp[j] + i//j
        # print(dp)
        return dp[-1]
            