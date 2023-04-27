class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        q = deque()
        self.lev = 0
        vis_cell = set()
        dl = [-1,-1,-1,0, 1,1,1,0]
        dr = [-1, 0,1,1,1,0,-1,-1]
        
        def bfs():
            while q:
                q_len = len(q)
                if (len(grid)-1, len(grid[0])-1) in vis_cell:
                    break
                flag = 0
                for _ in range(q_len):
                    node = q.popleft()
                    r, c = node
                    for i in range(8):
                        j = r + dl[i]
                        k = c + dr[i]
                        if j<0 or j==len(grid) or k<0 or k== len(grid[0]) or grid[j][k] != 0:
                            continue
                        if (j,k) not in vis_cell:
                            flag =1
                            vis_cell.add((j,k))
                            q.append((j,k))
                if not flag:
                    self.lev = -2
                    break
                else:
                    self.lev+=1
                
        if grid[0][0] != 0:
            return -1
        else:
            q.append((0, 0))
            vis_cell.add((0, 0))
            bfs()
        return self.lev+1