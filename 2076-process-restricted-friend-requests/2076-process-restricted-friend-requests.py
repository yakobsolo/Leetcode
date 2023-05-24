class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        rep = {i:i for i in range(n)}
        
        dic = defaultdict(set)

        
        def find(n):
            if n == rep[n]:
                return n
            rep[n] = find(rep[n])
            return rep[n]
        
        def union(x, y):
            par1 = find(x)
            par2 = find(y)
            
            rep[par2] = par1
           
            
        
        restrictions = {(i, j) for i,j in restrictions}
        
        ans = [False for _ in range(len(requests))]
        for k in range(len(requests)):
            i, j = requests[k]
            if (i, j) not in restrictions and (j, i) not in restrictions:
                merged = set()
                p1 = find(i)
                p2 = find(j)
                for b in range(n):
                    fi = find(b)
                    if fi == p1 or fi == p2:
                        merged.add(b)
                  
                for u, v in restrictions:
                    if u in merged and v in merged:
                        break
                else:
                    union(i, j)
                    ans[k] = True
                        
        return ans
        
        
        