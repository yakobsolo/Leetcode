class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leng = len(nums)
        prefix, suffix = [nums[0]], [nums[leng-1]]
        
        for i in range(1, leng):
            prefix.append(prefix[i-1] * nums[i])
        prefix.append(1)
        
        for j in range(leng-2, -1, -1):
            suffix.append(suffix[-1] * nums[j])
        
        suffix = suffix[-1::-1]
        suffix.append(1)

        ans = []
        for i in range(leng):
            ans.append(prefix[i-1]*suffix[i+1])
        return ans
            
        
            
            
        