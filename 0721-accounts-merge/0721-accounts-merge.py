
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        hash = defaultdict(set)
        leng = len(accounts)
        
        for i in range(leng):
            hash[(i, accounts[i][0])] = set(accounts[i][1:])
                
        rep = {(i,j): (i,j) for i, j in hash}
    
        def find(n):
            if n == rep[n]: return n
            rep[n] = find(rep[n])
            return rep[n]
        
        def union(x, y):
            
            par1 = find(x)
            par2 = find(y)
            
            rep[par1] = par2
            
        for key in hash:
            for k in hash:
                if key != k and key[1] == k[1]:
                    for i in hash[key]:
                        if i in hash[k]:
                            union(key, k)
                            break
        
        ans = []
        for par in rep:
            x = find(par)
            hash[x].update(hash[par])
            
        for par in rep:
            
            if par == rep[par]:
                arr = [par[1]] + list(sorted(list(hash[par])))
                ans.append(arr)
                
        return ans
              