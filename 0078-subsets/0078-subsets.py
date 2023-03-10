class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def issubsets(index, path):
            if index >= len(nums):
                ans.add(tuple(path[:]))
                return 
            
            
            for i in range(index, len(nums)):
                issubsets(i+1, path + [nums[i]])
                issubsets(i+1, path)
                
           
        issubsets(0, [])
        return list(ans)