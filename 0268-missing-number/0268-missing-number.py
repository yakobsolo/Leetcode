class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n
        
        for i in range( n):
            total = total ^ nums[i] ^ i
        return total
        