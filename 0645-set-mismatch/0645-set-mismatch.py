class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        i = 0
        duplicate,missed = -1, -1
        n = len(nums)
        while i < n:
            
            pos = nums[i] -1
            if pos != i:
                if nums[i] == nums[pos]:
                    duplicate = nums[i]
                    missed = i
                    i+=1
                else:
                    nums[i], nums[pos] = nums[pos] , nums[i]
                    if pos < i:
                        missed = i
                        
            else:
                i +=1
        return [duplicate, missed+1]
                
                
            