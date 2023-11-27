class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        
        ans  = 0
        l = 0
        N = len(nums)
        nice= 0
        for r in range(N):
            
            if nums[r] & nice == 0:
                nice |= nums[r]
                ans = max(ans, r-l+1)
            
            else:
                while l<r and nums[r]&nice != 0:
                    nice&=(~nums[l])
                    l+=1
            
            nice |= nums[r]
            # print(r, nice)
        return ans
            
            
            