class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        n, m = len(grid), len(grid[0])
        visted = set()
        
          
        def dfs(i, j):
            if (i<0 or i>=n or j<0 or j>=m) or (i, j)  in visted or grid[i][j] == 0:
                return 
            
            visted.add((i, j))
            grid[i][j] = 0
            # print(i,j)
            # print(grid)
            for r, c in directions:
                r, c = i+r, j+c
                
                dfs(r, c)
        
        
        
        
        
        
        for j in range(m):
            if grid[0][j] == 1 :
                dfs(0, j)
        for j in range(m):
            if grid[n-1][j] == 1 :
                dfs(n-1 ,j)
        for i in range(n):
            if grid[i][0] == 1:
                dfs(i, 0)
        for i in range(n):
            if grid[i][m-1] == 1 :
                dfs(i, m-1)
                
        count_ones = 0
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count_ones += 1
                    
        return count_ones 
        
        
                

                
            
                
                    
                    
                