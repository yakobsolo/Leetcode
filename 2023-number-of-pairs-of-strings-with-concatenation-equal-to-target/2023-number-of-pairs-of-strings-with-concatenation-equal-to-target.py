class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        from collections import Counter
        
        count = Counter(nums)
        
        n = len(nums)
        t = len(target)
        ans = 0
        for i in range(n):
            cur = nums[i]
            c = len(cur)
            if c < t:
                if target[:c] == cur:
                    after = target[c:]
                    if after != cur:
                        ans += count[after]
                    else:
                        if count[after]:
                            ans+=count[after]-1
        return ans
                