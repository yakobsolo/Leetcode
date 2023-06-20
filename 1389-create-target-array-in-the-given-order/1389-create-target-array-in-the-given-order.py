class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        for i in range(n):
            res.insert(index[i], nums[i])
        return res[:n]