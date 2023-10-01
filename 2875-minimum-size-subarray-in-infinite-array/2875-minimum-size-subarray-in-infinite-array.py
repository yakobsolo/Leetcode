class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        tot = sum(nums)
        ans =0
        if target%tot == 0:
            return n*(target//tot)
        if target > tot:
            ans= n*(target//tot)
            target = target%tot
        
        nums= nums+nums
        l = 0
        window = 0
        # print(target, nums, tot)
        temp = inf
        for r in range(len(nums)):
            window +=nums[r]
            # print(window)
            while l<n+n and window>target:
                window-=nums[l]
                # print(window, r, l)
                l+=1
            if window == target:
                temp = min(temp, r-l+1)
        return -1 if temp == inf else ans+temp
            
            
            