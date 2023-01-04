class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        count = Counter(nums)
        sums = 0
        for i in nums:
            if count[i] == 1:
                sums += i
        return sums