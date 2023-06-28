class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        n , m = len(s), len(t)
        if not s: return True
        if n>m: return False
        
        while j<m:
            if i== n: return True
            if s[i] == t[j] and m-j >=n-i:
                i+=1
            j+=1
        if i == n: return True
        return False
                