class Solution:
    def isGood(self, nums: List[int]) -> bool:
        N = len(nums)-1
        nums.sort()
        flg = True
        if N == 0: return False
        for i in range(N+1):
            
            if i<N:
                if i+1 != nums[i]:
                    flg = False
                    break
            else:
                
                if nums[i] != N: 
                    
                    flg = False
        
        if flg: return True
        return False
                
                
        