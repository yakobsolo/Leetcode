class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = 0
        h = len(nums) -1 
        minn = h
        maxx = 0
        
        if target not in nums:
            return [-1, -1]
        
        while l<= h:
            mid = (l + h)//2
            if nums[mid] > target:
                h = mid -1
            elif nums[mid] < target:
                l= mid + 1
            else:
                minn = min(minn, mid)
                h = mid -1
         
        l = 0
        h = len(nums) -1     
        while l<= h:
            mid = (l + h)//2
            if nums[mid] > target:
                h = mid -1
            elif nums[mid] < target:
                l= mid + 1
            else:
                
                maxx = max(maxx, mid)
                l = mid +1
        return [minn, maxx]