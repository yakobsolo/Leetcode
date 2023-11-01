class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        
        init = (1<<20)-1
        
        cur = init
        count = 0
        for i in range(N):
            cur&=nums[i]
            if cur == 0:
                
                count+=1
                cur = init
                
        return count+1 if cur!=init and count==0 else count
                
                
            
            
        