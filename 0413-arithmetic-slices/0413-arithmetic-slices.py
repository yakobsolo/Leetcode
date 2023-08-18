class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        sums = 0
        if n >= 2:
            prev = nums[1] - nums[0]
        
        l = 0
        for i in range(2, n):
            cur = nums[i]-nums[i-1]
            if cur != prev:
                print(i)
                k = i - l 
                sums+= (k-2)*(k-1)//2
                
                l = i-1
            prev = cur
        if n>2 and  l != i-1:
            k = i - l +1
            sums+= (k-2)*(k-1)/2
                
        return int(sums)
            
            