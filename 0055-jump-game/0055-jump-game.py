class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        destination = n-1
        # if n ==1: return True
        for i in range(n-2, -1, -1):
            if i + nums[i] >= destination:
                destination = i
        if destination == 0 : return True
        return False