class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visted = set()
        
        def permutation(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in visted:
                    path.append(nums[i])
                    visted.add(nums[i])
                    permutation(path)
                    path.pop()
                    visted.discard(nums[i])
        permutation([])
        return ans
                