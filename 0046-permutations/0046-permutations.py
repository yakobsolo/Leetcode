class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        lis = []
        visted = set()
        
        def permutation(nums):
            
            if len(lis) == len(nums):
                ans.append(lis[::])
                return
                    
            for i in range(len(nums)):
                if nums[i] not in visted:
                    
                    lis.append(nums[i])
                    visted.add(nums[i])
                    permutation(nums)
                    lis.pop()
                    visted.discard(nums[i])

                
                
        permutation(nums)
        return ans