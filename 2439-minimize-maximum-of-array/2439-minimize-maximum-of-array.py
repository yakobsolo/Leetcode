class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        first = -1
        prefix_sum = 0
        for i in range(len(nums)):
            curr = nums[i]
            prefix_sum += curr
            first = max(first, ceil(prefix_sum / (i + 1)))


        return first