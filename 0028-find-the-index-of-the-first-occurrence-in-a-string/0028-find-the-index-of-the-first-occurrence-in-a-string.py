class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        i =n-1
        hash = 0
        for c in needle:
            hash += (26**i) *ord(c)
            i-=1
            hash%=(10**9+7)
            
            
        j =i = n-1
        find = 0
        window= 0
        indx = 0
        for c in haystack:
            if window<=i:
                find += (26**j) * ord(c)
                window+=1
                j-=1
                find %=(10**9+7)
                
                if window>i and find == hash:
                    return indx
                
            else:
                minus = ((26**i)*ord(haystack[indx]))
                find -= minus
                find *=26 
                find += ord(c)
            
                find%=(10**9+7)
                indx+=1
                if find == hash:
                    return indx
        return -1
                
                
                
            
            
            