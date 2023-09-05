class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r  = 0, len(nums)-1
        ans = nums[0]
        
        
        
        while l<=r:
            mid = l+(r-l)//2
            
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                # print(mid)
                r = mid-1
                ans = min(ans, nums[mid])
            
            
        return ans