class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        n, m = len(grid), len(grid[0])
        count_fresh = 0
        for i in range(n):
            for j in range(m):
                count_fresh +=1
                if grid[i][j] == 2:
                    queue.append((i, j))
        lev = 0
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        
        def isValid(i, j):
            return (i>=0 and i<n and j>=0 and j<m) and grid[i][j] == 1
        while queue:
            leng = len(queue)
            for _ in range(leng):
                r, c = queue.popleft()
                for i, j in directions:
                    i, j = r+i, c+j
                    if isValid(i, j):
                        grid[i][j] = 0
                        queue.append((i, j))
            lev+=1
        
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1
        return lev -1 if lev else 0
                    
            
            
            