class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        def issubsets(index, path):
            if index >= len(nums):
                
                ans.add(tuple(path[::]))
                return 
            
            
            path.append(nums[index])
            issubsets(index+1, path)
            path.pop()
            issubsets(index+1,path)
        issubsets(0, [])
        return list(ans)