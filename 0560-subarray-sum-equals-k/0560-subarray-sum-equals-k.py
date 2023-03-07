class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix= {0: 1}
        diff = 0
        currsum  = 0
        res = 0
        for i in nums:
            currsum += i
            diff = currsum - k
            res += prefix.get(diff, 0)
            prefix[currsum] = prefix.get(currsum, 0) + 1
        return res
            