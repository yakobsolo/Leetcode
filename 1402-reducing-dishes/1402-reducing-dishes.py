class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        N = len(satisfaction)
        mx = 0
        satisfaction.sort()
        for i in range(N):
            cur = 0
            k = 1
            for j in range(i, N):
                cur +=(satisfaction[j]*(k))
                mx = max(mx, cur)
                k+=1
            
        return mx