class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        heap = []
        heappush(heap, (0, 0, 0))
        n, m = len(grid), len(grid[0])
        
        dist  = [[inf]*m for i in range(n)]               
        def isValid(x, y):
            return (0<=x<n and 0<=y<m)
        ans= 0
        visted = set()
        while heap:
            cost, r, c = heappop(heap)
            
            ans = max(ans, cost)
            if (r, c) == (n-1, m-1): return cost
            
            for i in range(4):
                x, y = r+directions[i][0], c+directions[i][1]
                if isValid(x, y):
                    if grid[r][c] == i+1 and cost < dist[x][y]:
                        dist[x][y] = cost
                        heappush(heap, (cost, x, y))
                    else:
                        if cost+1 < dist[x][y]:
                            dist[x][y] = cost+1
                            heappush(heap, (cost+1, x, y))
                    
                        
            