class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        nextsmaller = []
        leng = len(nums)
        
        minn = -inf
        
        for i in range(leng-1, -1, -1):
            if nums[i] < minn:
                return True
            while nextsmaller and nextsmaller[-1] < nums[i]:
                minn = nextsmaller.pop()
            nextsmaller.append(nums[i])
                
                
        return False