class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n , m = len(grid), len(grid[0])
        direction= [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dist = [[float("inf")]*m for i in range(n)]
        
        def isValid(x, y):
            return (0<=x<n and 0<=y<m)
        dist[0][0] = grid[0][0]
        heap = [[dist[0][0], 0, 0]]
        
        while heap:
            
            obs , r, c = heappop(heap)
            
            if (r, c) == (n-1, m-1): return obs
            
            for i in range(4):
                x, y = r+direction[i][0], c+direction[i][1]
                
                if isValid(x, y) and grid[x][y] + obs < dist[x][y]:
                    dist[x][y] = grid[x][y] + obs
                    heappush(heap,[dist[x][y], x, y])