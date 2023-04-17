class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m , n = len(grid), len(grid[0])
        maxarea = 0
        
        dl = [-1, 0, 1, 0]
        dr = [0, 1, 0, -1]
        def dfs(r, c):
            if not  ((0<= r< m) and (0<=c<n) ) or not grid[r][c] : return 0
            if grid[r][c] == -1: return 0
            
            grid[r][c] = -1
            
            count = 0
            for i in range(4):
                count += dfs(r+dl[i], c+dr[i])
            return count+1
        
        for r in range(m):
            for c in range(n):
                if grid[r][c]:
                    maxarea = max(maxarea, dfs(r, c))
        return maxarea