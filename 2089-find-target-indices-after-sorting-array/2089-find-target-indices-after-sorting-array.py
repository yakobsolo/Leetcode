class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        srt_i = []
        nums.sort()
        for i in range(0, len(nums)):
            if nums[i] == target:
                srt_i.append(i)
        return sorted(srt_i)

obj1 = Solution()
target = 2
nums = [1,2,5,2,3]
obj1.targetIndices(nums, target)