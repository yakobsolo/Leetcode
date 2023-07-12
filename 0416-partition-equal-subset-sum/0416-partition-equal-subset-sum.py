class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums%2 != 0: return False
        n = len(nums)
        dp = set()
        dp.add(0)
        target = sums//2
        for i in range(n):
            tmp = set()
            for val in dp:
                cur = nums[i] +val
                if cur == target: return True
                tmp.add(cur)
            dp.update(tmp)
        return False