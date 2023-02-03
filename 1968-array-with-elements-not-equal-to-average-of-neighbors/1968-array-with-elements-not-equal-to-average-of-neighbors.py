class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        
        l,r = 0, len(nums)-1
        while len(res) != len(nums):
            res.append(nums[l])
            l+=1
            
            if l<=r:
                res.append(nums[r])
                r-=1
        return res
        
        
        
        
        
        
#         r = len(nums) -2
#         for i in range(1,len(nums) -1):
#             averg = (nums[i-1]+nums[i+1])/2
#             if nums[i] == averg:
#                 if (nums[i-1]+nums[r+1])/2 == nums[r]:
#                     nums[i-1], nums[r+1] = nums[r+1], nums[i-1]
#                 elif (nums[i-1]+nums[r-1])/2 == nums[r]:
#                     nums[i-1], nums[r-1] = nums[r-1], nums[i-1]
#                 else:
#                     nums[i-1], nums[r+1] = nums[r+1], nums[i-1]
        
        
#         return nums