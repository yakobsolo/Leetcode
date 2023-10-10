class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        i =n-1
        hash = 0
        N = len(haystack)
        if i+1>N: return -1
        for c in needle:
            hash += (26**i) *ord(c)
            i-=1
            
            hash%=(10**9+7)
        j =i = n-1
        find = 0
        w= 0
        indx = 0
        # print(hash)
        for c in haystack:
            if w<=i:
                find += (26**j) * ord(c)
                w+=1
                j-=1
                find %=(10**9+7)
                
                if w>i and find == hash:
                    return indx
                # print(find, w, i)
            else:
                minus = ((26**i)*ord(haystack[indx]))
                find -= minus
                find *=26 
                find += ord(c)
                # print(c, find, minus)
                # find*=26
                find%=(10**9+7)
                indx+=1
                if find == hash:
                    return indx
        return -1
                
                
                
            
            
            