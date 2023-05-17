class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        dl = [0, 1]
        dr = [1, 0]
        rank = {(i, j): 1 for i in range(n) for j in range(m)}
        rep = {(i, j): (i, j) for i in range(n) for j in range(m)}
        
        
        
        
        def find(node):
            if rep[node] == node:
                return node
            rep[node] = find(rep[node])
            return rep[node]
        
        
        def union(x, y):
            
            par1 = find(x)
            par2 = find(y)
            # print(par1, par2, "p")
            
            if par1 != par2:
                if rank[par1] >= rank[par2]:
                    # print("j")
                    rep[par2] = par1
                    rank[par1] +=  rank[par2]
                else:
                    rep[par1] = par2
                    rank[par2] += rank[par1]
            else:
                return True
            return False            
        
        directions = {1: [(1,3,5), ()],
                      2: [(), (2,5,6)],
                      3: [(), (2,5,6)],
                      4: [(1,3,5),(2,5,6)],
                      6: [(1,3,5),()]
                        }
        
        for i in range(n):
            for j in range(m):
                cur = grid[i][j]
                if cur == 5: continue
                r =j+dr[0]
                b = i+dl[1]
                # print((i, j))
                if 0<= r <m:
                    right = grid[i][r]
                    if right in directions[cur][0]:
                        # print(i, r)
                        union((i,j), (i, r))
                if 0<= b< n:
                    bottom = grid[i+dl[1]][j+dr[1]]
                    if bottom in directions[cur][1]:
                        print(b, j)
                        union((i, j), (b, j))
                
                
                
                
        # print(rep)
        if find((0, 0)) == find((n-1, m-1)):
            return True
        return False
            
        