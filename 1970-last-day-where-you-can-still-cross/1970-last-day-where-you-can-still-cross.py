class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        rep = {(i, j):(i, j) for i in range(row) for j in range(col)}
        mat= []
        for i in range(row):
            roww = [0] * col
            mat.append(roww)
        
        def find(n):
            if n == rep[n]: return n
            rep[n] = find(rep[n])
            return rep[n]
        
        def union(x, y, r, c):
            par1  = find((x, y))
            par2  = find((r, c))
            
            
            if (par1[0] == 0 and par2[0] == row-1) or par1[0] == row-1 and par2[0] == 0: return True
            if par1[0] == 0 or par1[0] == row-1:
                rep[par2] = par1
            else:
                rep[par1] = par2
        
        def isvalid(r, c):
            if 0<= r< row and 0<= c< col and mat[r][c]: return True
            
        dl = [-1, 0, 1, 0]
        dr = [0, 1, 0, -1]
        
        for i in range(len(cells) -1, -1, -1):
            r, c = cells[i]
            mat[r-1][c-1] = 1
            for z in range(4):
                j ,k = r + dl[z], c+dr[z]
                if isvalid(j-1, k-1):
                    end = union(r-1, c-1, j-1, k-1)
                    if end:
                        return i
            