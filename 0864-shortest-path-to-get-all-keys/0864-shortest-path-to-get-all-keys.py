class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
         
        n = len(grid)
        m = len(grid[0])
        keySet = set(['a','b','c','d','e','f'])
        lockSet = set(['A','B','C','D','E','F'])
        
        
        keyCount = 0
         
        q = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    q.append((i, j, ""))
                elif grid[i][j] in keySet:
                    keyCount += 1
        
        
        visited = set()
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        
        def addAllDirections(i,j,keyStr):
            for d in directions:
                r = i+d[0]
                c = j+d[1]
                    
                
                if r<0 or c<0 or r>=n or c>=m:
                    continue
                q.append((r,c,keyStr))
                
        steps = 0
        
        while q:
            q_len= len(q)
                
            for _ in range(q_len):
                i,j,keyStr = q.popleft()
                
                if (i,j,keyStr) in visited or grid[i][j] == '#':
                    continue
                
                c = grid[i][j]
                if c in lockSet:
                    if c.lower() not in keyStr:
                        continue
                    else: 
                        addAllDirections(i,j,keyStr)
                elif c in keySet:
                    if c not in keyStr:
                        keyStr += c
                        if len(keyStr) == keyCount:
                            return steps
                        addAllDirections(i,j,keyStr)
                    else:
                        addAllDirections(i,j,keyStr)
                else:
                    addAllDirections(i,j,keyStr)
            
                visited.add((i,j,keyStr))
              
            steps += 1    
        
        return -1
                
        