class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letthash = {}
        res = 0 
        
        l = 0
        for r in range(len(s)):
            letthash[s[r]] = 1 + letthash.get(s[r], 0)
            
            while (r-l+1) - max(letthash.values()) > k:
                letthash[s[l]] -= 1
                l +=1
        
        
            res = max(res, r-l+1)
        return res