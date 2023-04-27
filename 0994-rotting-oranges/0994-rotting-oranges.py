class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh = 0
        rl = len(grid)
        cl = len(grid[0])
        queue = deque()
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 1:
                    fresh +=1
                if grid[i][j] == 2:
                    queue.append([i,j])
        time = 0
        dl = [-1, 0, 1, 0]
        dr = [0, 1, 0, -1]
        
        while queue and fresh>0:
            que_len = len(queue)
            for i in range(que_len):
                

                r, c = queue.popleft()
                for i in range(4):
                    
                    j, k= r+dl[i], c+dr[i]
                    if not ((0<= j< rl) and (0 <= k< cl)) or grid[j][k] != 1:
                        continue
                        
                    fresh -= 1
                    queue.append([j, k])
                    grid[j][k] = 2

            time+=1
        if fresh == 0:
            return time
        else:
            return -1