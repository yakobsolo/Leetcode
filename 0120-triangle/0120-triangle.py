class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        n = len(triangle)
        def dp(i, j):
            if i== n: 
                return 0
         
            if (i, j) not in memo:
                memo[(i, j)] = min(dp(i+1, j), dp(i+1, j+1))+triangle[i][j]
                
            return memo[(i, j)]
        return dp(0, 0)