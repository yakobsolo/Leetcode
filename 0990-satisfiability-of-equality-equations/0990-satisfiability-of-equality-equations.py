class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        let = ["a", "b", "c", "d", "e", "f", "g", "h","i", "j", "k", "l", "m" ,"n", 'o', "p", "q", 'r', "s","t", "u","v", "w","x", "y","z"] 
        rep = {v:v for i, v in enumerate(let)}
        rank = {v:1 for i , v in enumerate(let)}
        
        def find(n):
            if n == rep[n]:
                return n
            rep[n] = find(rep[n])
            return rep[n]
        
        def union(x, y):
            par1 = find(x)
            par2 = find(y)
            
            if par1 != par2:
                if rank[par1] <= rank[par2]:
                    rep[par2] = par1
                    rank[par1] +=1
                else:
                    rep[par1] = par2
                    rank[par2] +=1
                
        arr = []            
        for exp in equations:
            sign = exp[1:3]
            if sign == "==":
                union(exp[0], exp[3])
            else:
                arr.append([exp[0], exp[3]])
        for u, v in arr:
            if find(u) == find(v):
                return False
        return True