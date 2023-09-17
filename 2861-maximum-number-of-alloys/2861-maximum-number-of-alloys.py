class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def isPossible(m, mt):
            tot = 0
            for i in range(n):
                tot += max((composition[mt][i] * m - stock[i]) * cost[i] , 0)
            return tot<=budget
                           
        
        
        def max_alloy_make(mt):
            l, r = 0 , 10**16
            
            while l<r:
                mid = l+ (r-l+1)//2


                if isPossible(mid, mt):
                    l=mid
                else:
                    r=mid-1
            return l
            
            
            
            
        max_alloy = 0
        for machine_type in range(k):
            max_alloy = max(max_alloy, max_alloy_make(machine_type))
        return max_alloy
            