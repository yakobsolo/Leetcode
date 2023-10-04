class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        n , m = len(grid), len(grid[0])
        direction= [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def isValid(x, y):
            return (0<=x<n and 0<=y<m)
        
        heap = [[0, 0, 0]]
        ans = 0
        visted = set()
        while heap:
            
            obs , r, c = heappop(heap)
            
            ans = max(obs, ans)
            if (r, c) == (n-1, m-1): return ans
            if (r, c) in visted: continue
            visted.add((r,c))
            for i in range(4):
                x, y = r+direction[i][0], c+direction[i][1]
                
                if isValid(x, y) and (x, y) not in visted:
                    num_obs = max(obs, grid[x][y]+obs)
                    heappush(heap,[num_obs, x, y])