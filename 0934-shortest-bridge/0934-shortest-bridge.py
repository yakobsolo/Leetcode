class Solution(object):
    def shortestBridge(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        dl = [-1, 0, 1, 0]
        dr = [0, 1, 0, -1]
        def dfs(r, c):
            path = []
            grid[r][c] = -1
            path.append((r, c))
            
            for i in range(4):
                i ,j = r+dl[i], c+dr[i]
                if i<0 or i>= len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != 1: continue
                    
                if grid[i][j] == 1:
                    path += dfs(i, j)
                    
            return path
        def bfs(q):
            lev = 0
            visted = set()
            q = deque(q)
            while q:
                q_len = len(q)
  
                for i in range(q_len):
                    r, c = q.popleft()
                    visted.add((r, c))
                
                    for i in range(4):
                        k, j = r+ dl[i], c+ dr[i]
                        if k<0 or k>=len(grid) or j<0 or j>=len(grid[0]) or (k, j) in visted: continue
                        
                        visted.add((k, j))
                        q.append((k, j))
                        if grid[k][j] == 1:
                            return lev
                lev+=1
                        
            
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    
                    path = dfs(i, j)
                    return bfs(path)
                    