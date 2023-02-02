class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        res = 0
        r = len(nums) -1
        nums.sort()
        
        
        for i, l in enumerate(nums):
            while i<=r and l+nums[r] > target:
                r -=1
            
            if i<=r:
                res+= (2**(r-i))
                 
                
        return res % (10**9+7)
    
        