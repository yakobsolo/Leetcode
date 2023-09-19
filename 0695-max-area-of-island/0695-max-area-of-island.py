class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n , m = len(grid), len(grid[0])
        max_area = 0
        visted = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def dfs(i, j):
            
            visted.add((i, j))
            area = 0
            for k in range(4):
                r, c = i+directions[k][0], j+directions[k][1]
                
                if r>=0 and r<n and c>=0 and c<m and grid[r][c] != 0 and (r, c) not in visted:
                    area += dfs(r, c)
                    
                    
            return area+1
                    
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0 and (i, j) not in visted:
                    # print(i, j)
                    max_area = max(max_area, dfs(i, j))
                    # print(max_area)
        return max_area