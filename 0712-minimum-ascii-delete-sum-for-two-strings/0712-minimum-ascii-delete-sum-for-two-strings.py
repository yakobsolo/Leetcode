class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:

        all_ascii = 0
        for c in s1:
            all_ascii+=ord(c)
        for c in s2:
            all_ascii+=ord(c)
            
        
        n, m = len(s1), len(s2)
        
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(n-1, -1, -1):
            for j in range(m-1,-1, -1):
                if s1[i] == s2[j]:
                    dp[i][j]= dp[i+1][j+1] + ord(s1[i])
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
        return all_ascii - 2*dp[0][0]
            
        