class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(1, len(nums)):
            if nums[i-1] == nums[i]:
                nums[i-1] *= 2
                nums[i] = 0
        ptr = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[ptr], nums[i] = nums[i], nums[ptr]
                ptr+=1
        return nums