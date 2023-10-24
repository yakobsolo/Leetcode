class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        
       

        count = Counter(nums)
        freq = count.values()
        if len(count) == 1:return 1
        
        res = len(nums)
        mx = min(freq)
        
        def helper(partition):
            res = 0
            for f in freq:
                group = f//partition
                rem = f%partition
                
                if rem>group:return inf
                
                res += ceil(f /(partition+1))
            return res
        for i in range(1, mx+1):
            
            res = min(res, helper(i))
        return res
        