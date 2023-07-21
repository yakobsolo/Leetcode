class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = list()
        for num in nums:
            num = list(str(num))
            for n in num:
                ans.append(int(n))
        return ans
                