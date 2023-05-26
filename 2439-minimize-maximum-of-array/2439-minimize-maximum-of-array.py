class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        first = nums[0]
        prefix_sum = nums[0]

        for i in range(1, len(nums)):
            curr = nums[i]
            prefix_sum += curr
            if curr > first:
                first = max(first, ceil(prefix_sum / (i + 1)))


        return first