class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
        for l in range(1, n):
            for r in range(n-l):
                if s[r] == s[r+l]:
                    dp[r][r+l] = dp[r+1][r+l-1] + 2
                else:
                    dp[r][r+l] = max(dp[r][r+l-1], dp[r+1][r+l])
        return dp[0][n-1]
                
