class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first , second , third = 0, 0, 0
        
        n = len(nums)
        
        first = nums[0]
        flag = 1
        for i in range(1, n):
            cur = nums[i] 
            # print(cur)
            if cur <= first:
                first = cur
                continue
            if not second and flag:
                second = cur
                flag = 0
                continue
            # print(first, second, nums[i])
            if cur > second: return True
            second = cur
        return False
            
                            