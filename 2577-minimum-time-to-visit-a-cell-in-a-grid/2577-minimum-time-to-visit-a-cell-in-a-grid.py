class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        n, m = len(grid), len(grid[0])
        
        heap = [(0, 0, 0)]
        
        dist = [[inf]*m for _ in range(n)]
        def isValid(x, y):
            return 0<=x<n and 0<=y<m
        
        k, p = 0, 0
        flag = 0
        for i ,j in directions:
            i, j = k+i, p+j
            if isValid(i, j) and grid[i][j]<=1: 
                flag= 1 
                break
        if not flag: return -1
        while heap:
            t, r, c = heappop(heap)
            
            if (r, c) == (n-1, m-1): return t
            
            for i in range(4):
                x, y = r+ directions[i][0], c+ directions[i][1]
                
                if isValid(x, y):
                    if t+1 >= grid[x][y]:
                        if t+1 < dist[x][y]:
                            dist[x][y] = t+1
                            heappush(heap, (t+1, x, y))
                    else:
                        temp = grid[x][y] - t
                        if (temp)%2 == 0:
                            if grid[x][y]+1 < dist[x][y]:
                                dist[x][y] = grid[x][y]+1
                                heappush(heap, (grid[x][y]+1, x, y))
                        else:
                            if grid[x][y]< dist[x][y]:
                                dist[x][y] = grid[x][y]
                                heappush(heap, (grid[x][y], x, y))
                                
                            
                            
                    