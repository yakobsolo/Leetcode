class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letthash = {}
        res = 0 
        
        l = 0
        maxf= 0
        for r in range(len(s)):
            letthash[s[r]] = 1 + letthash.get(s[r], 0)
            maxf = max(maxf, letthash[s[r]])
            while (r-l+1) - maxf > k:
                letthash[s[l]] -= 1
                l +=1
        
        
            res = max(res, r-l+1)
        return res