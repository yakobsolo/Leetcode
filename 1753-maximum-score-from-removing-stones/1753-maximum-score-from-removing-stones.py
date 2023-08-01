class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        nums = [a,b, c]
        nums.sort()
        count = 0
        while len(nums) >=2 :
            if nums[0]:
                if nums[-1]:
                    count+=1
                    nums[-1]-=1
                    nums[0] -=1
                else:
                    nums.pop()
            else:
                nums.pop(0)
            nums.sort()
        return count