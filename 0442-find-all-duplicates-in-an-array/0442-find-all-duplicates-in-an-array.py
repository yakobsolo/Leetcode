class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ans = set()
        n = len(nums)
        i = 0
        while i < n:
            if nums[i]-1 != i:
                swapposition = nums[i] -1
                if nums[i] == nums[swapposition]:
                    ans.add(nums[i])
                    i += 1
                    
                else:
                    nums[i], nums[swapposition] = nums[swapposition], nums[i]
            else:
                i +=1
        return list(ans)