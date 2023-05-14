class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        dl = [-1, 0, 1, 0]
        dr = [0, 1, 0, -1]
        q = deque()
        row = len(maze)
        col = len(maze[0])
        q.append(entrance)
        lev = 0
        visted = set()
        while q:
            q_len = len(q)
            for _ in range(q_len):
                r, c  = q.popleft()
                for i in range(4):
                    i, j = r+dl[i], c+dr[i] 
                    if 0<= i <row and 0<=j < col:
                        if (i, j) not in visted and maze[i][j] == ".":
                            q.append((i, j))
                            visted.add((i, j))
                    elif [r, c] != entrance:
                        return lev
                    
                        
            lev +=1
            
        return -1