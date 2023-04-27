class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        prev = defaultdict(tuple)
        def shortestpath():
            while q:
                node = q.popleft()
                if node == (len(grid)-1, len(grid[0])-1):
                    break
                r, c = node
                
                dl = [-1, -1, -1, 0, 1, 1, 1, 0]
                dr = [-1, 0, 1, 1, 1, 0, -1, -1]
                
                for i in range(8):
                    
                    j= r + dl[i]
                    k = c+ dr[i]
                    
                    if not (0<= j<len(grid) and 0<=k< len(grid[0])) or grid[j][k] !=  0:
                        continue
                    q.append((j, k))
                    prev[(j, k)] = (r, c)
                    grid[j][k] = 1

                
            
            
        if grid[0][0] == 0: 
            q.append((0,0))
            prev[(0, 0)] = (-1, -1)
            grid[0][0] = 1
            shortestpath()
        else:
            return -1
        
        if (len(grid)-1, len(grid[0])-1) not in prev:
            return -1
        
        cur = (len(grid)-1, len(grid[0])-1)
        ans = []
        
        while cur != (-1, -1):
            ans.append(cur)
            cur = prev[cur]
        return len(ans)
    