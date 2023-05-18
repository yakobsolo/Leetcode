class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s_len = len(s)
        rep = {i:i for i in range(s_len)}
        rank = {i: 1 for i in range(s_len)}
        
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
        
        for u, v in pairs:
            union(u, v)
        
        order = defaultdict(list)
        for i in range(s_len):
            par = find(i)
            order[par].append(s[i])
        ans = ""
        for key in order:
            order[key].sort(reverse=True)
        
        for i in range(s_len):
            ans+= order[find(i)].pop()
        return ans
            