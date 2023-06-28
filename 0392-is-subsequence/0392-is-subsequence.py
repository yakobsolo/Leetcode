class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        n , m = len(s), len(t)
        if not s: return True
        
        
        while j<m:
            
            if s[i] == t[j]:
                i+=1
                if i==n: return True
            j+=1
        
        return False
                