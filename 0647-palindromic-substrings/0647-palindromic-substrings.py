class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        def countpalindrome(s, l, r):
            res = 0
            while l>=0 and r<n and s[l] == s[r]:
                res +=1
                l-=1
                r+=1
            return res
            
        for i in range(n):
            ans += countpalindrome(s, i, i)
            
            ans += countpalindrome(s, i, i+1)
        return ans