class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        tot = sum(nums)
        i = 0
        while i < n:
            if nums[i] > 0:
                break 
            elif k > 0:
                tot += (2*-nums[i])
                k -= 1
            else:
                break
            i+=1
        if  k%2 == 1:
            if i == n:
                tot-= (2*-nums[i-1])
            elif i > 0 and -nums[i-1] < nums[i]:
                tot += (2*nums[i-1])
            
            else:
                tot -= (2*nums[i])
        return tot
   