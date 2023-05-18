class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        rep , rank ={}, {}
        rep = {v:v for v in range(1, n+1)}
        rank = {v:1 for v in range(1, n+1)}
        
        def find(n):
            if n == rep[n]: return n
            rep[n] = find(rep[n])
            return rep[n]
        
        def union(x, y):
            par1 = find(x)
            par2 = find(y)
            
            if rank[par1] <= rank[par2]:
                rep[par2] = par1
                rank[par1] +=1
            else:
                rep[par1] = par2
                rank[par2] +=1
                
                        
        for a, b, d in roads:
            union(a, b)
            
        ans  = inf
        for a, b, d in roads:
            if find(a) == find(b) == find(1):
                ans = min(ans, d)
        return ans
            