class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1]*len(nums)
        increasing = []
        for j in range(2):
            
            for i in range(len(nums)):
                while increasing and nums[increasing[-1]] < nums[i]:
                    top = increasing.pop()
                    ans[top] = nums[i]
                increasing.append(i)
       
        return ans