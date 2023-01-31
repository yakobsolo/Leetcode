class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        temp = 0
        sums = sum(nums)
        for i in range(len(nums)):
            sums -= nums[i]
            if sums == temp:
                return i
            temp += nums[i]
        return -1
            
            
        