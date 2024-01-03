class Solution:
    def lastSubstring(self, s: str) -> str:
        ans = ""
        N = len(s)
        maxc = max(s)
        for i in range(N):
            if s[i] == maxc:
                ans = max(ans, s[i:])
        return ans
                