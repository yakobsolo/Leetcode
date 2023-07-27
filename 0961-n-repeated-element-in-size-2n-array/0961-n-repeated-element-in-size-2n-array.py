class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        visted = set()
        for n in nums:
            if n not in visted:
                visted.add(n)
            else:return n