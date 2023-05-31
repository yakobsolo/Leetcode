class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dic = {}
        def countpalindrome(s, l, r):
            res = 0
            while l>=0 and r<n and s[l] == s[r]:
                res = r-l+1
                dic[res] = s[l:r+1]
                l-=1
                r+=1
                
            return res
        max_len = 0   
        for i in range(n):
            odd = countpalindrome(s, i, i)
            
            even = countpalindrome(s, i, i+1)
            max_len= max(odd, even, max_len)
        return dic[max_len]