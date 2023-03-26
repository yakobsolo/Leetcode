class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        def recursive(idx, path):
            if idx == len(nums):
                if len(path) >= 2:
                    ans.add(tuple(path[::]))
                return
            
            if not path or nums[idx] >= path[-1]:
                recursive(idx+1, path + [nums[idx]])
                
            recursive(idx+1, path)
            
        recursive(0, [])
        print(ans)
        return list(ans)