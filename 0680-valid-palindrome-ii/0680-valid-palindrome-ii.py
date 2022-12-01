class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0,len(s)-1
        count = 0
        while l<r:
            if s[l] != s[r]:
                l2,r2,l3,r3 = l+1,r,l,r-1
                first, second = True, True
                while l2<r:
                    if s[l2] != s[r]:
                        first = False
                    l2+=1
                    r-=1
                while l3< r3:
                    if s[l3] != s[r3]:
                        second = False
                        break
                    l3+=1
                    r3-=1
                if first or second:
                    return True
                else:
                    return False
                
            
                
            l+=1 
            r-=1
        return True