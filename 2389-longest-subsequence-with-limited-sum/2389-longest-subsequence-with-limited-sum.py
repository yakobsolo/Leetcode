class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefixsum = []
        prefixsum.append(nums[0])
        for i in range(1, len(nums)):
            prefixsum.append(prefixsum[-1] + nums[i])
        
        ans = []
        for j in range(len(queries)):
            leng = 0
            for k in range(len(prefixsum)):
                
                if queries[j] >= prefixsum[k]:
                    leng +=1
            ans.append(leng)
            
        return ans
            