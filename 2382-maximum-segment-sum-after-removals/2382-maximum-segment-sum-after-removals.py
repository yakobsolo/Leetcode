class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
       
        
        leng = len(nums)
        rank = [n for n in nums]
        rep = {i:i for i in range(leng)}
        
        def find(n):
            if n == rep[n]: return n
            rep[n] = find(rep[n])
            return rep[n]
        
        def union(x, y):
            par1 = find(x)
            par2 = find(y)
            
            rep[par2] = par1
            rank[par1] += rank[par2]

            
        res = [0]
        
        arr = [0]*leng
        heap = []
        import heapq
        def isvalid(idx):
            if 0<= idx< leng and arr[idx]: return True
            
        
        max_rank = 0
        for i in range(leng-1, 0, -1):
            p = removeQueries[i]
            arr[p] = 1
            l, r = p -1, p+1
            
            if isvalid(l):
                union(l, p)
                
            if isvalid(r):
                union(p, r)
            max_rank = max(max_rank, rank[find(p)])
            res.append(max_rank)
        return reversed(res)
            
            