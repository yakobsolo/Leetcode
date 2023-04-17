class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        peri = 0
        rowleng = len(grid)
        colleng = len(grid[0])
        
        dl = [-1, 0, 1, 0]
        dr = [0, 1, 0, -1]
        def dfs(r, c):
            if not ((0<= r<rowleng) and (0<= c< colleng)) or not grid[r][c]: return 1
            if grid[r][c] == -1: return 0
            
            grid[r][c] = -1
            count = 0
            for i in range(4):
                count += dfs(r + dl[i], c+dr[i])
            return count
        
        for r in range(rowleng):
            for c in range(colleng):
                if grid[r][c]: return dfs(r, c)
                