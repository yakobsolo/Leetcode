class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def issubsets(index, path):
            if index >= len(nums):
                ans.append(path[::])
                return 
            
            
            path.append(nums[index])
            issubsets(index+1, path)
            path.pop()
            issubsets(index+1,path)
        issubsets(0, [])
        return ans