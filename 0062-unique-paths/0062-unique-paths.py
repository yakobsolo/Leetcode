class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # dp = [0 for i in range(m) for j in range(n)]
        dp = []
        for i in range(m):
            arr = [0] *n
            dp.append(arr)
        dp[-1][-1] = 1
        
        def lookup(r, c):
            if 0<=r<m and 0<=c<n: return dp[r][c]
            return 0
        for i in range(m-1, -1, -1):
            
            for j in range(n-1, -1, -1):
                dp[i][j] += lookup(i+1, j) + lookup(i, j+1)
            
        return dp[0][0]
            
            