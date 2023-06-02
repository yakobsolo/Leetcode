class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [0] *(n+1)
        
        for i in range(n-1, -1, -1):
            row = triangle[i]
            
            for j, v in enumerate(row):
                dp[j] = min(dp[j], dp[j+1])+row[j]
        return dp[0]