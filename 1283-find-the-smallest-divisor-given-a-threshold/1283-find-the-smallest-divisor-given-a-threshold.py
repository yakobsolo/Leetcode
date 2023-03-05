class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        l = 1
        h = max(nums)
        minn = h
        leng = len(nums)
        
        while l<= h:
            mid =(l+h)//2
            
            quocients = 0
            for i in range(leng):
                quocients +=ceil(nums[i]/mid)
                
            
            if quocients > threshold:
                l = mid + 1
            else:
                minn = min(minn, mid)
                h =mid -1
        return minn