class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        s_len = len(source)
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
                if rank[par1] >= rank[par2]:
                    rep[par2] = par1
                    rank[par1] += 1
                else:
                    rep[par1] = par2
                    rank[par2] +=1
        
        
        for u, v in allowedSwaps:
            union(u, v)
        
        order = defaultdict(set)
        order_target = defaultdict(set)
        for i in range(s_len):
            par = find(i)
            order[par].add(source[i])
            order_target[par].add(target[i])
        
        res = 0
        
        count = Counter(target)
        for i in range(s_len):
            par = find(i)
            if  source[i] not in order_target[par]:
                res +=1
            else:
                count[source[i]] -=1
                if count[source[i]] == 0:
                    order_target[par].discard(source[i])
                
        return res
            