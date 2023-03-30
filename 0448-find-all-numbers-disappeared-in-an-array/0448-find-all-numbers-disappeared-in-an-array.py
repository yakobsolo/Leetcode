class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        missed = set()
        i = 0
        while i < n:
            if nums[i] != i+1:
                correctposition = nums[i] -1
                if nums[i] == nums[correctposition]:
                    i +=1
                else:
                    nums[correctposition], nums[i] = nums[i] , nums[correctposition]          
            else:
                i +=1   
        ans = []
        print(nums)
        for i in range(n):
            if nums[i] != i+1:
                ans.append(i+1)
        return ans