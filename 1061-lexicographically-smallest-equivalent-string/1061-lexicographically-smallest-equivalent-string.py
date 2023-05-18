class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        rep = {chr(v):chr(v) for v in range(ord("a"), ord("z")+1)}
        rank= {v:1 for v in rep}
        
        def find(n):
            if n == rep[n]:
                return n
            rep[n] = find(rep[n])
            return rep[n]
        
        def union(x, y):
            par1 = find(x)
            par2 = find(y)
            min_ = min(par1, par2, x, y)
            rep[par1] , rep[par2], rep[x], rep[y]= min_, min_, min_, min_
#             if par1!=par2:
#                 if rank[par1]<= rank[par2]:
#                     rep[par2] = par1
#                     rank[par1] +=1
#                 else:
#                     rep[par1] = par2
#                     rank[par2] +=1
            
        
        res = ""
        # print(rep)
        for i in range(len(s1)):
            union(s1[i], s2[i])
        for c in baseStr:
            res+=find(c)
        return res
            
            