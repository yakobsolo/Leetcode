class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        queue = deque()
        n =len(grid)
        if grid[0][0] == 1 : return -1
        if grid[0][0] == 0 and n == 1:return 1
        
        queue.append((0, 0))
        visted = set()
        visted.add((0, 0))
        
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
        lev = 1
        
        def isValid(i, j):
            return i>=0 and i<n and j>=0 and j<n and (i, j) not in visted
        
        while queue:
            q_len = len(queue)
            
            for _ in range(q_len):
                
                r, c = queue.popleft()
               
                for i, j in directions:
                    
                    i, j = i+r, j+c
                    
                    if isValid(i, j):
                            if grid[i][j] == 0:
                        
                                if (i, j) == (n-1, n-1): return lev+1
                                queue.append((i , j))
                            visted.add((i, j))
            lev+=1
      
        return -1
        
        