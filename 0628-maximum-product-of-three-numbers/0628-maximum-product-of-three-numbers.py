class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)
        nums.remove(max2)
        max3 = max(nums)
        
        nums.append(max2)
        min1 = min(nums)
        nums.remove(min1)
        min2 = min(nums)
        
        return max(min1*min2*max1, max1*max2*max3)