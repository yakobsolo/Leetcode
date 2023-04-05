class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def issubset(index, path):
            if index == len(nums):
                temp = []
                for i in range(path.bit_length()):
                    if path & (1<<i):
                        temp.append(nums[i])
                ans.append(temp[:])
                return 
            
            issubset(index+1, path | (1<<index))
            issubset(index+1, path)
        issubset(0, 0)
        return ans