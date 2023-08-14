class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        from collections import Counter
        
        count = Counter(nums)
        for n in nums:
            if count[n] == 1: return n