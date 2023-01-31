class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        temp = 0
        ans = 1
        minpos = 1
        for i in range(len(nums)):
            temp += nums[i]
            minpos = min(minpos, temp)
        if minpos<1:
            ans = abs(minpos)+1
       
        return ans
        