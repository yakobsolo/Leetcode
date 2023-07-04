class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        
        count = Counter(nums)
        nums = sorted(list(set(nums)))
        n = len(nums)
        dp1, dp2 = 0, 0
        for i in range(n):
            cur = count[nums[i]]*nums[i]
            if i > 0 and nums[i] == nums[i-1]+1:

                temp = dp2
                dp2 = max(cur+dp1, dp2)
                dp1 = temp
            else:
                temp = dp2
                dp2 = cur+dp2
                dp1 = temp

        return dp2
        