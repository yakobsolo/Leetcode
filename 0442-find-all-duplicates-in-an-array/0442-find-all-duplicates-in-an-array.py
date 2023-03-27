class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = list()
        n = len(nums)
        i = 0
        while i < n:
            if nums[i]-1 != i and nums[i]> 0:
                swapposition = nums[i] -1
                if nums[i] == nums[swapposition]:
                    ans.append(nums[i])
                    nums[i] = -1*nums[i]
                    i += 1    
                else:
                    nums[i], nums[swapposition] = nums[swapposition], nums[i]
            else:
                i +=1
        return ans