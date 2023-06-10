class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        expected = [[1, 2, 3], [4, 5, 0]]
        if board == expected: return 0
        q = collections.deque()
        for i in range(2):
            for j in range(3):
                if board[i][j] == 0:
                    
                    q.append((i, j, board))
                    
                    break
        lev = 0
        
        dl = [-1, 0, 1, 0]
        dr = [0, 1, 0, -1]
        visted = set()
        while q:
            q_len  = len(q)
            
            for _ in range(q_len):
                i, j, b= q.popleft()
                
                for k in range(4):
                    r, c = dl[k]+i , dr[k] + j
                    if 0<=r<2 and 0<=c<3:
                    
                        new_b = [row[:] for row in b]
                        new_b[i][j], new_b[r][c] = new_b[r][c], new_b[i][j]
                        if new_b==expected: return lev+1
                        if str(new_b) not in visted:
                            q.append((r, c, new_b))
                            visted.add(str(new_b))
            lev +=1
            
        return -1