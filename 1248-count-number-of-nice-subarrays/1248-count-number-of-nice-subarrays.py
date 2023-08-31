class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        countnotodd = defaultdict(int)
        countnotodd[0] = 1
        currodd = 0
        diff = 0
        for i in nums:
            if i%2 == 1:
                currodd += 1
            countnotodd[currodd] += 1
            if currodd >= k:
                diff = currodd - k
                res += countnotodd[diff]
                
        return res