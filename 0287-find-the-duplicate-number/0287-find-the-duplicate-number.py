class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        
        i = 0
        while i < n:
            if nums[i] != i +1:
                correctposition = nums[i] -1 
                if nums[i] == nums[correctposition]:
                    i +=1
                else:
                    nums[correctposition], nums[i] = nums[i] , nums[correctposition]
                    
            else: 
                i +=1
        return nums[-1]
                