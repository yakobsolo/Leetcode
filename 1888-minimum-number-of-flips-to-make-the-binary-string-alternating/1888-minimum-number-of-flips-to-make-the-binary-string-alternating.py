class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s+s
        atr1, atr2 = "", ""
        res = len(s)
        l = 0
        
        for i in range(len(s)):
            atr1 += "1" if i%2 else "0"
            atr2 += "0" if i%2 else "1"
            
        
        dif1, dif2 = 0, 0
        for r in range(len(s)):
            if atr1[r] != s[r]:
                dif1 +=1
            if atr2[r] != s[r]:
                dif2 +=1
                
            if (r-l +1) > n:
                if s[l] != atr1[l]:
                    dif1 -=1
                if s[l] != atr2[l]:
                    dif2 -=1
                l+=1
            if r-l+1 ==n:
                res = min(res, dif1, dif2)
        return res
                
            
            
            