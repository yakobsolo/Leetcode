class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        currodd = 0
        diff = 0
        for i in nums:
            if i%2 == 1:
                currodd += 1
            prefix[currodd] = prefix[currodd] + 1
            if currodd >= k:
                diff = currodd - k
                res += prefix[diff]
        return res