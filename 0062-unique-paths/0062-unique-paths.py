class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visted = set()
        memo = {}
        dl = [0, -1]
        dr = [-1, 0]
        def dp(cell):
            if cell == (0, 0): return 1
            i, j  = cell
            
            if i<0 or i>= m or j< 0 or j>=n: return 0
            if (i, j) not in memo:
                memo[(i,j)] = dp((i + dl[0], j + dr[0])) + dp((i + dl[1], j+dr[1]))
            
            return memo[(i,j)]

        return dp((m-1, n-1))
            
            