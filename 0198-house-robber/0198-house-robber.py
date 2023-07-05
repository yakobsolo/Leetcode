class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n==2: return max(nums[0], nums[1])
        if n==1: return nums[0]
        earn1, earn2 = nums[0], max(nums[1], nums[0])
        for i in range(2, n):
            temp=earn2
            earn2 = max(earn2, earn1+nums[i])
            earn1=temp
        return earn2
