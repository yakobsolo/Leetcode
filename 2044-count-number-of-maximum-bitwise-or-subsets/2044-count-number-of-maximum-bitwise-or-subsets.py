class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        
        leng = len(nums)
        maxor = 0
        for i in range(leng):
            maxor |= nums[i]
        
        
        totsub = pow(2, leng)
        count = 0
        
        for i in range(1, totsub):
            sub = 0
            for j in range(leng):
                if (i & (1<<j)):
                    sub |= nums[j]
            if sub == maxor:
                count +=1
        return count
            