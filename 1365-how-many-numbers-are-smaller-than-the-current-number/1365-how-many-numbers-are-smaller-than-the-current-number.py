class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        copy = sorted(nums)
        lis =[]
        for i in nums:
            lis.append(copy.index(i))
        return lis