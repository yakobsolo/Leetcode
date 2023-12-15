class Solution:
    def maxJump(self, stones: List[int]) -> int:
        
        N = len(stones)
        if N < 3:
            return stones[-1]-stones[-2]
        ans = 0
        for i in range(N-1, -1, -1):
            ans = max(ans, stones[i]-stones[i-2])
        return ans    
            