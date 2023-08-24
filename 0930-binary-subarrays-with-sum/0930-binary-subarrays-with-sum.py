class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        n = len(nums)
        def helper(goal):
            sm = 0
            count = 0
            l = 0
            for r in range(n):
                sm +=nums[r]
                while l<=r and sm>goal:
                    sm -= nums[l]
                    l +=1
                count +=(r-l)+1
            return count
        return abs(helper(goal-1) - helper(goal))
