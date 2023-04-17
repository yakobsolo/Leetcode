class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m = len(grid1)
        n = len(grid1[0])
        count = 0
        dl = [-1, 0, 1, 0]
        dr = [0, 1, 0, -1]
        
        def dfs(r, c):
            if not (0<= r < m and 0<= c < n) or not grid2[r][c]: return 
            if grid2[r][c] == -1: return
         
            grid2[r][c] = -1
            if not grid1[r][c]:
                self.flag = 0
                
            for i in range(4):
                dfs(r+dl[i], c+dr[i])
                
                
        for r in range(m):
            for c in range(n):
                self.flag = 1
                if grid2[r][c] == 1:
                    dfs(r, c)
                    if self.flag: count +=1
                        
        return count