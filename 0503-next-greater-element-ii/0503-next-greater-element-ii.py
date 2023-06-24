class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack, nextgreater = [], [-1 for i in range(n)]
        for _ in range(2):
            for i in range(n):
                while stack and nums[stack[-1]] < nums[i]:
                    top = stack.pop()
                    nextgreater[top] = nums[i]
                    
                stack.append(i)
        return nextgreater