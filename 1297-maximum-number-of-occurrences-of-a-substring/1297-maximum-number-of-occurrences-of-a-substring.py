class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        
        hash = defaultdict(int)
        
        l = 0
        N = len(s)
        
        visted = defaultdict(int)
        uniq = 0
        for r in range(N):
            visted[s[r]]+=1
            if len(visted) <= maxLetters and r-l+1 <= maxSize and r-l+1 >= minSize:
                hash[s[l:r+1]]+=1
                visted[s[l]]-=1
                if visted[s[l]]  == 0:
                    del visted[s[l]]
                    
                l+=1
            if len(visted) > maxLetters or r-l+1 > maxSize: 
                visted[s[l]]-=1
                if visted[s[l]]  == 0:
                    del visted[s[l]]
                l+=1
                
        mx = 0
        for k, v in hash.items():
            mx  = max(mx, v)
        return mx
                
                
            