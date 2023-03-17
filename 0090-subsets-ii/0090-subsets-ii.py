class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        def issubsets(index, path):
            if index == len(nums):
                
                ans.append(path[:])
                return 
            
            
            path.append(nums[index])
            issubsets(index+1, path)
            while index < len(nums)-1 and nums[index] ==  nums[index+1]:
                index+=1
                
            path.pop()
            issubsets(index+1,path)
        issubsets(0, [])
        return list(ans)