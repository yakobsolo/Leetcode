class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        second = -inf 
        stack = []
        n = len(nums)
        for i in range(n-1, -1, -1):
            if nums[i] < second: return True
            while stack and stack[-1] < nums[i]:
                second = stack.pop()
            stack.append(nums[i])
        return False