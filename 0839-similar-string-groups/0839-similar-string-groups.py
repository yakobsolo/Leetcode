class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        rep = {c:c for c in strs}
        rank = {c:1 for c in strs}
        
        def find(s):
            if rep[s] == s:
                return s
            rep[s] = find(rep[s])
            return rep[s]
    
        def union(c1, c2):
            par1 = find(c1)
            par2 = find(c2)
            
            if par1!= par2:
                if rank[par1] >= rank[par2]:
                    rep[par2] = par1
                    rank[par1]+=1
                else:
                    rep[par1] = par2
                    rank[par2]+=1
            return 
        
        
        N = len(strs)
        for i in range(N):
            for j in range(i, N):
                
                
                c= 0
                for k in range(len(strs[i])):
                    if strs[i][k] != strs[j][k]:
                        c+=1
                if c<=2:
                    union(strs[i], strs[j])
        
        hash = defaultdict(int)
        for c in strs:
            hash[find(c)] +=1
        return len(hash)
            