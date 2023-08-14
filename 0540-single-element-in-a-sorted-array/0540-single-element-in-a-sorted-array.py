class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0 , n-1
        
        while l<=r:
            mid = l + (r - l)//2
            
            if mid -1 < 0 or mid + 1 == n or  nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1]: return nums[mid]
            
            leftsize = mid-1 if nums[mid-1] == nums[mid] else mid
            
            if leftsize%2:
                r = mid -1
            else: l = mid +1
        
            
                        
                        
                    