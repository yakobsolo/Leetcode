class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        j = 0 << n
        for i in range(n):
            if (j & (1 << nums[i])) != 0:
                return nums[i]
            j |= (1<< nums[i])
        

            
                