class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.visted = 0
        
        def permutation(path):
            if self.visted.bit_count() == len(nums):
                ans.append(path[:])
                return
            
            for i in range(len(nums)):
                if not (self.visted & (1<<i)):
                    path.append(nums[i])
                    self.visted |= (1<<i)
                    permutation(path)
                    path.pop()
                    self.visted &= ~(1<<i)
        permutation([])
        return ans
                