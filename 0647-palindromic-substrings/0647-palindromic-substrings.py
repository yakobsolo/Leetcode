class Solution:
    def countSubstrings(self, s: str) -> int:
        def ispalindrome(s):
            l, r= 0, len(s)-1
            while l< r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        n = len(s)
        count = 0
        for i in range(n):
            for j in range(i, n):
                if ispalindrome(s[i:j+1]):
                    count+=1
        return count