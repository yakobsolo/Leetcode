class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l, r = 0, n-1
        
        while l<r:
            
            mid = l + (r-l)//2
            
            if nums[mid] > nums[r]:
                l = mid +1
            else:
                r = mid
        
        if target >= nums[r] and target <= nums[n-1]:
            l = r
            r = n-1
        elif target >= nums[0] and target <= nums[r-1]:
            l = 0
        else:
            return -1
        while l<=r:
            mid = l + (r-l)//2
            
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid +1
            else:
                r = mid -1
        return -1
        
        
        
            
        