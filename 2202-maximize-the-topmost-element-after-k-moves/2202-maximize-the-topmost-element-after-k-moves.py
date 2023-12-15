class Solution:
    def maximumTop(self, nums: List[int], k: int) -> int:
        N = len(nums)
        if k==0: return nums[0]
        if k>N:
            if N==1 and k%2==1:return -1
            return max(nums)
        
        if k == 1:
            if N ==1:
                return -1
            return nums[1]
        
        mx = max(nums[:k-1])
        if N>=k+1:
            return max(mx, nums[k])
        return mx