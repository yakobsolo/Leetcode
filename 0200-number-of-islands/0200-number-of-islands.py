class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        count = 0
        dl = [-1, 0, 1, 0]
        dr = [0, 1, 0 , -1]
        
        def dfs(r, c):
            if not (0<= r< m and 0<= c< n) or grid[r][c] == "0":
                return 
            if grid[r][c] == -1:
                return 
            
            grid[r][c] = -1
            self.flag = 1
            
            for i in range(4):
                dfs(r +dl[i], c + dr[i])
                
        for r in range(m):
            for c in range(n):
                self.flag = 0
                
                if grid[r][c] == "1":
                    
                    dfs(r, c)
                    if self.flag:
                        count +=1
        return count