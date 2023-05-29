class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums%2 != 0: return False
        
        n = len(nums)
        final = set()
        final.add(0)
        
        target = sums//2
        for i in range(n):
            temp = set()
            for j in final:
                cur = nums[i] + j
                if cur == target: return True
                temp.add(cur)
            final.update(temp)
        return False