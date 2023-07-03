class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        dp = [1]*n
        pairs.sort()
        for i in range(1, n):
            f,s = pairs[i]
            for j in range(i-1, -1, -1):
                pf, ps = pairs[j]
                if ps < f:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)