class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        init = set(nums)
        i_len = len(init)
        count = 0
        for i in range(len(nums)):
            visted = set()
            for j in range(i, len(nums)):
                visted.add(nums[j])
                if len(visted) == i_len:
                    count +=1
        return count
                