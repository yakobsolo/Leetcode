class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        
        def compare(a, b):
            return nums[a]+nums[b] > nums[b]+nums[a]
        
        for a in range(len(nums) -1):
            b = a +1
            while b< len(nums):
                if not compare(a, b):
                    nums[a], nums[b] = nums[b], nums[a]
                b +=1
        return str(int("".join(nums)))
                    