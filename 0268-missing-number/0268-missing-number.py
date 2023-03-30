class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = 0
        given = nums[0]
        for i in range(1, n):
            total ^= i
            given ^= nums[i]
        total ^= n
        return total ^ given
        