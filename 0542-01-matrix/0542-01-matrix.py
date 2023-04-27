class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rl = len(mat)
        cl = len(mat[0])
        dl = [-1, 0, 1, 0]
        dr = [0, 1, 0, -1]
        q = deque()
        visted = set()
        for r in range(rl):
            for c in range(cl):
                if mat[r][c] == 0:
                    q.append((r,c))
                    visted.add((r, c))                    
                    
        d = 0
        while q:
            q_len = len(q)

            for _ in range(q_len):
                r, c  = q.popleft()
                
                flag = 0
                for i in range(4):
                    j = r + dl[i]
                    k = c + dr[i]

                    if j<0 or j== len(mat) or k<0 or k==len(mat[0]) or (j, k) in visted: continue
                    
                    visted.add((j,k))
                    mat[j][k] = d+1
                    q.append((j, k))
            d +=1
            
        
        
        
               
        return mat