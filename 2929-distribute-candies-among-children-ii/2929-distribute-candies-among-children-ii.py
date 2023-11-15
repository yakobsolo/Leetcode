class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        limit = min(limit, n)
        ans = 0
        for i in range(limit+1):
            if n-i > limit * 2:
                continue
            ans += (min(limit, n-i) - max(0, n-i-limit) + 1)
        return ans