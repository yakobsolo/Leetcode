class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        size = 0
        for ch in s:
            if ch.isdigit(): size*=int(ch)
            else: size+=1
        
        N = len(s)
        for i in range(N-1, -1, -1):
            if (k==0 or k==size) and s[i].islower():
                return s[i]
            elif s[i].isdigit():
                size = size//int(s[i])
                k%=size
            else: size-=1
                
                
        