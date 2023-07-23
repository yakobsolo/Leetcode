class Solution:
    def minOperations(self, nums: List[int]) -> int:
        op = 0
        n = len(nums)
        prev = nums[0]
        for i in range(1,n):
            
            if nums[i] <= prev:
                op+= prev - nums[i] +1
                prev +=1
            
            else: prev = nums[i]
        return op
                