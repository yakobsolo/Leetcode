class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rep = {(u, v):(u, v) for u, v in stones}
        rank = {(u, v):1 for u, v in stones}
        leng = len(stones)
        def find(i, j):
            if (i, j) == rep[(i, j)]: return (i, j)
            rep[(i, j)] = find(rep[(i, j)][0], rep[(i,j)][1])
            return rep[(i, j)]
        
        def union(r, c, i, j):
            par1 = find(r, c)
            par2 = find(i, j)
            
            if rank[par1] <= rank[par2]:
                rep[par2] = par1
                rank[par1] +=1
            else:
                rep[par1] = par2
                rank[par2] +=1
        
        row , col = defaultdict(int), defaultdict(int)
        row[stones[0][0]] = 0
        col[stones[0][1]] = 0
        
        for i in range(1, leng):
            r, c= stones[i]
            if r in row:
                union(r, c, stones[row[r]][0], stones[row[r]][1])
                row[r] = i
            else:
                row[r] = i
            if c in col:
                union(r, c, stones[col[c]][0], stones[col[c]][1])
                col[c] = i
            else:
                col[c] = i
        count = 0
        for key in rep:
            if key == rep[key]: count+=1
        
        return leng - count
                